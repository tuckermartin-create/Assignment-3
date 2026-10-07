def get_number(prompt, *, minimum=None, minimum_exclusive=False):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if minimum is not None and (
            value <= minimum if minimum_exclusive else value < minimum
        ):
            comparison = "greater than" if minimum_exclusive else "at least"
            print(f"Please enter a number {comparison} {minimum}.")
            continue
        return value


initial_revenue = get_number("Enter the initial annual revenue: $", minimum=0)
growth_rate = get_number(
    "Enter the annual growth rate (%): ", minimum=-100, minimum_exclusive=True
)

revenue = initial_revenue
growth_multiplier = 1 + growth_rate / 100

print("\nBusiness Growth Projection")
print("--------------------------")
print(f"{'Year':<6}{'Projected revenue':>20}")
print(f"{0:<6}${revenue:>19,.2f}")

for year in range(1, 11):
    revenue *= growth_multiplier
    print(f"{year:<6}${revenue:>19,.2f}")
