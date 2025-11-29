# chai = "Ginger Chai"

# def prepare_chai(order):
#     print(f"Preparing your {order}")

# prepare_chai(chai)
# print(chai)

chai = [1, 2, 3]

def edit_chai(cups):
    cups[1] = 42

edit_chai(chai)
print(chai)

def make_chai(tea, milk, suger):
    print(f"Making chai with {tea}, {milk}, {suger}")

make_chai("Darjeeling", "Full Cream", "2 spoons") #positional arguments

make_chai(milk="Skimmed", tea="Assam", suger="No sugar") #keyword arguments 

def special_chai(*ingredients, **extras):
    print("Ingredients: ", ingredients)
    print("Extras: ", extras)

special_chai("Cinnamon", "Cardamom", milk="Oat Milk", suger="Honey")

def chai_order(order= None):
    if order is None:
        order = []
    print(order)
chai_order("Masala Chai")
chai_order()