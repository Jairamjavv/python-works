from typing import Optional
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import create_engine, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, Session
from pydantic import BaseModel
from contextlib import asynccontextmanager


# pydantic objects
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str]


class ItemCreate(BaseModel):
    name: str
    description: Optional[str]


class ItemUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]


# database configuration
DATABASE_URI = "sqlite:///test.db"


class Base(DeclarativeBase):
    pass


class DBItem(Base):
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[Optional[str]]


engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# dependency to get the db session
def get_db():
    db = SessionLocal()
    try:
        yield db  # generator
    finally:
        db.close()


""" 
creating lifespan, which means certain code will run only once when the application starts up and clears it when the application ends
"""


# fastapi configuration
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


app = FastAPI(lifespan=lifespan)


# defining constants
httpexception_detail = "Item not found"


# defining routes
@app.get("/")
def read_root():
    return "Server is running"


@app.post("/items")
def create_item(item: ItemCreate, db: Session = Depends(get_db)) -> Item:
    db_item = DBItem(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)  # holds the ID generated
    db.close()
    return Item(**db_item.__dict__)


@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)) -> Item:
    db_item = db.query(DBItem).filter(DBItem.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail=httpexception_detail)
    db.close()
    return Item(**db_item.__dict__)


@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)) -> Item:
    db_item = db.query(DBItem).filter(DBItem.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail=httpexception_detail)
    for k, v in item.model_dump().items():
        setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    db.close()
    return Item(**db_item.__dict__)


@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)) -> Item:
    db_item = db.query(DBItem).filter(DBItem.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail=httpexception_detail)
    db.delete(db_item)
    db.commit()
    db.close()
    return Item(**db_item.__dict__)
