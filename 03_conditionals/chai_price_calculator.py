order = input("Choose your cup size (Small, Medium, Large): \n").lower()

if order == "small":
    print("The price is 10 rupees.")
elif order == "medium":
    print("The price is 15 rupees.")
elif order == "large":
    print("The price is 20 rupees.")
else:
    print("Invalid size selected.\n")