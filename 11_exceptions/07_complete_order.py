class InvalidChaiError(Exception): pass

def bill(flavour, cups):
    menu = {"masala": 20, "ginger": 40}
    try :
        if flavour not in menu:
            raise  InvalidChaiError("That chai is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be integer")
        total = menu[flavour] * cups
        print(f"Your bill for {cups} cups of {flavour} chai is {total}")

    except Exception as e:
        print("Error: ", e)
    finally:
        print("Thank You for visiting my shop")
    
bill("ginger", 2)
bill("mint", 2)
bill("masala", "two")