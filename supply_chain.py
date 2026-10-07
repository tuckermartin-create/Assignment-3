warehouses = [
    {"name": "Warehouse A", "inventory": {"apples": 100, "bananas": 150}},
    {"name": "Warehouse B", "inventory": {"apples": 200, "bananas": 100}},
]

total_stock = {}

for warehouse in warehouses:
    for product, quantity in warehouse["inventory"].items():
        total_stock[product] = total_stock.get(product, 0) + quantity

print("Total stock across the supply chain:")
for product, quantity in total_stock.items():
    print(f"{product}: {quantity}")
