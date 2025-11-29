favorite_teas = [
    "Masala Chai",
    "Green Tea",
    "Lemon Tea",
    "Masala Chai",
    "Green Tea",
    "Elaichi Chai"
]

unique_chai = {chai for chai in favorite_teas if len(chai) > 10}
print(unique_chai)

recipes = {
    "Masala Chai" : ["ginger", "Cardamom", "Black Pepper"],
    "Elaichi Chai" : ["Elaichi", "Milk", "water"],
    "Kesar Chai" : ["Kesar", "Cardamom", "Milk"]
}

unique_spices = {spice for ingrediants in recipes.values() for spice in ingrediants}

print(unique_spices)