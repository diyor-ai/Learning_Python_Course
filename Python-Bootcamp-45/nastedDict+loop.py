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
for key, value in store.items():
    stock = value['stock']
    for val in value.items():
        print(stock)
