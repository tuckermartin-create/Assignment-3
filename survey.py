preferences = ["coffee", "tea", "coffee", "soda"]

counts = {}
for preference in preferences:
    counts[preference] = counts.get(preference, 0) + 1

total_responses = len(preferences)

for product, count in counts.items():
    market_share = count / total_responses * 100
    print(f"{product}: {market_share:g}%")
