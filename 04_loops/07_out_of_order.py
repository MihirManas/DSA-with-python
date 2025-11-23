flavours = ["Ginger", "Lemon", "Masala", "Elaichi", "Discontinued", "Mint", "Out of Stock"]

for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        print("Discointinued flavour found.")
        break
    print(f"Preparing {flavour} tea.")

print(f"Out side of loop.")