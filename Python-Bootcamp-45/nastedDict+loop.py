store = {
    "electronics": {
        "phone": {"price": 1000, "stock": 5},
        "laptop": {"price": 2000, "stock": 3}
    },
    "clothes": {
        "shirt": {"price": 50, "stock": 20}
    }
}

total_stock = 0
for stocks in store.values():
    for value in stocks.values():
        total_stock += value["stock"]
print(f"Total stock: {total_stock}")

# find most expensive product

for value in store.values():
    for x in value.values():
        max_value = x["price"]
        if x["price"] > max_value:
            max_value = x["price"]
    print(f"Max price: {max_value}")


for stocks in store.values():
    for key, value in stocks.items():
        if value["stock"] > 5:
            print(f"{key}: {value['stock']}")