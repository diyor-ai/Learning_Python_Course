store = {
    "electronics": {
        "phone": {"price": 1000, "stock": 5},
        "laptop": {"price": 200, "stock": 3}
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

max_price = 0
most_expensive = None

for category in store.values():
    for product_name, info in category.items():
        if info["price"] > max_price:
            max_price = info["price"]
            most_expensive = product_name

print("Most expensive:", most_expensive, max_price)

for stocks in store.values():
    for key, value in stocks.items():
        if value["stock"] > 5:
            print(f"{key}: {value['stock']}")
