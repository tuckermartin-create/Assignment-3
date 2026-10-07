customer_purchases = {
    "Alice": 750,
    "Bob": 2500,
    "Carol": 6200,
    "David": 1200,
    "Eve": 400,
}

tiers = {"Bronze": 0, "Silver": 0, "Gold": 0}

for customer, total_purchases in customer_purchases.items():
    if total_purchases < 1000:
        tier = "Bronze"
    elif total_purchases < 5000:
        tier = "Silver"
    else:
        tier = "Gold"

    tiers[tier] += 1
    print(f"{customer}: {tier}")

print("\nCustomer counts by tier:")
for tier, count in tiers.items():
    print(f"{tier}: {count}")
