names = ["Hitesh", "Mihir", "Sriya", "Anita"]
bills = [50, 70, 100, 1200]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees.")