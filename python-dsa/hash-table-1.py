sample_stock_market_data: list[list] = [
    ["12052024", 135],
    ["13052024", 138],
    ["14052024", 132],
]


def give_stock_price(key: str):
    for stock in sample_stock_market_data:
        if stock[0] == key:
            return stock[1]
    return -1


print(give_stock_price("13052024"))
