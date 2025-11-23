# value = 13
# reminder = value%5

# if reminder:
#     print(f"Not divisible, remainder is {reminder}")

value = 13

if (reminder := value%5):
    print(f"Not divisible, remainder is {reminder}")



available_sizes = ["S", "M", "L", "XL", "XXL"]

if (requested_size := input("Enter size: ").upper()) not in available_sizes:
    print(f"Size {requested_size} not available.")
else:
    print(f"Delivering size {requested_size}.")
    

available_flavours = ["Ginger", "Lemon", "Masala", "Elaichi", "Mint"]

print("Available flavours: ", available_flavours)

while(flavours:= input("Enter flavour: ").title()) not in available_flavours:
    print(f"{flavours} chai is not available. Please choose from the available flavours.")

print(f"Preparing {flavours} tea.")