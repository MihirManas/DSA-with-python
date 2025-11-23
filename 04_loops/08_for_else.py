staff = [("Amit", 25), ("Zara", 22), ("Lina", 19)]

for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to vote.")
        break
else:
    print("No eligible voters found.")