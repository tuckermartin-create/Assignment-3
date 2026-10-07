def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if value <= 0:
            print("Please enter a number greater than 0.")
            continue
        return value


def get_non_negative_number(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if value < 0:
            print("Please enter a number greater than or equal to 0.")
            continue
        return value


def calculate_repayment_months(loan_amount, annual_interest_rate, monthly_payment):
    monthly_rate = annual_interest_rate / 100 / 12
    if monthly_payment <= loan_amount * monthly_rate:
        raise ValueError("The monthly payment must be greater than the first month's interest.")

    balance = loan_amount
    months = 0
    while balance > 0:
        interest = balance * monthly_rate
        balance = round(balance + interest - monthly_payment, 2)
        months += 1

    return months


loan_amount = get_positive_number("Enter the loan amount: $")
annual_interest_rate = get_non_negative_number("Enter the annual interest rate (%): ")
monthly_payment = get_positive_number("Enter the monthly payment: $")

try:
    months = calculate_repayment_months(
        loan_amount, annual_interest_rate, monthly_payment
    )
except ValueError as error:
    print(error)
else:
    print(f"It will take {months} months to pay off the loan.")
