from unittest import TestCase
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker
from .main import DBItem, app, Base, get_db

client = TestClient(app)

DATABASE_URI = "sqlite:///:memory:"
engine = create_engine(
    DATABASE_URI,
    connect_args={
        "check_same_thread": False,
    },
    poolclass=StaticPool,  # static connection
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db  # generator
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


class MainTest(TestCase):
    def setUp(self):
        Base.metadata.create_all(bind=engine)

        # create test items
        session = TestingSessionLocal()
        db_item = DBItem(id=100, name="test_item", description="This is a test item")
        session.add(db_item)
        session.commit()
        session.close()

        return super().setUp()

    def tearDown(self):
        Base.metadata.drop_all(bind=engine)

    # testing the "/" route
    def test_read_root(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "Server is running")

    def test_create_item(self):
        response = client.post(
            "/items/", json={"name": "test_name", "description": "this is a test item"}
        )
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["name"], "test_name")
        self.assertEqual(data["description"], "this is a test item")
        self.assertIn("id", data.keys())

    def test_read_item(self):
        # Create an item
        response = client.post(
            "/items/", json={"name": "Test Item", "description": "This is a test item"}
        )
        assert response.status_code == 200, response.text
        data = response.json()
        item_id = data["id"]

        response = client.get(f"/items/{item_id}")
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["name"] == "Test Item"
        assert data["description"] == "This is a test item"
        assert data["id"] == item_id

    def test_update_item(self):
        item_id = 1
        response = client.put(
            f"/items/{item_id}",
            json={"name": "Updated Item", "description": "This is an updated item"},
        )
        assert response.status_code == 404, response.text
        data = response.json()
        # assert data["name"] == "Updated Item"
        # assert data["description"] == "This is an updated item"
        # assert data["id"] == item_id

    def test_delete_item(self):
        item_id = 1
        response = client.delete(f"/items/{item_id}")
        assert response.status_code == 404, response.text
        data = response.json()
        # assert data["id"] == item_id
        # Try to get the deleted item
        response = client.get(f"/items/{item_id}")
        assert response.status_code == 404, response.text


if __name__ == "__main__":
    main_test = MainTest()
    main_test.test_read_root()
