menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced peach tea",
    "Ginger Tea"
]

iced_tea = [tea for tea in menu if "Iced" in tea and len(tea) == 14]

print(iced_tea)