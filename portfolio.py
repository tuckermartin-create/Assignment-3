import random


portfolio = {
    "AAPL": {"shares": 10, "price": 170},
    "TSLA": {"shares": 4, "price": 250},
    "AMZN": {"shares": 2, "price": 130},
}


def calculate_portfolio_value():
    total_value = 0
    for stock in portfolio.values():
        total_value += stock["shares"] * stock["price"]
    return total_value


print(f"Initial portfolio value: ${calculate_portfolio_value():,.2f}")

for day in range(1, 8):
    for stock in portfolio.values():
        daily_change = random.uniform(-0.05, 0.05)
        stock["price"] *= 1 + daily_change
    print(f"Day {day} portfolio value: ${calculate_portfolio_value():,.2f}")
