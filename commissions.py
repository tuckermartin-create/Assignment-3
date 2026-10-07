sales = {"Alice": 5000, "Bob": 7000, "Carol": 3000}


def calculate_commission(sales_amount):
    return sales_amount * 0.10


commissions = {}
for employee, sales_amount in sales.items():
    commissions[employee] = calculate_commission(sales_amount)

print("Commission Leaderboard")
print("----------------------")
for rank, (employee, commission) in enumerate(
    sorted(commissions.items(), key=lambda item: item[1], reverse=True),
    start=1,
):
    print(f"{rank}. {employee}: ${commission:.2f}")
