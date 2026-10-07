projected_revenue = [30000, 50000, 80000]
scale = 10000

print("Projected Revenue by Year")
for year, revenue in enumerate(projected_revenue, start=1):
    bar_length = round(revenue / scale)
    bar = ""
    for _ in range(bar_length):
        bar += "#"
    print(f"Year {year}: {bar}")
