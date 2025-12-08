chai_menu = {"masala" : 30, "Ginger": 40}

try:
    chai_menu["elaichi"]
except KeyError:
    print("The key that you want to acess that doesn't excits")