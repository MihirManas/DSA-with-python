snack = input("Enter Your Prefered snack: \n").lower()

print(f"user said: {snack}")
if snack == "cookies" or snack == "samosa":
    print(f"Great choice ! we'll serve you {snack}")
else:
    print("Sorry we don't have that snack, you can try out cookies or samosa")