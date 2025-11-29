def chai_cutomer():
    print("Welcome ! what chai would you like to take\n")
    order = yield
    while True:
        print(f"preparing: {order}")
        order = yield

stall = chai_cutomer()
next(stall) # start the generator

stall.send("masala chai")
stall.send("lemon chai")