expenses = {
    "Travel": [500, 200],
    "Meals": [40, 60, 30],
    "Supplies": [100],
}

grand_total = 0

print("Expense Summary Report")
print("----------------------")

for category, amounts in expenses.items():
    category_total = 0
    for amount in amounts:
        category_total += amount
    grand_total += category_total
    print(f"{category}: ${category_total:.2f}")

print("----------------------")
print(f"Grand total: ${grand_total:.2f}")
