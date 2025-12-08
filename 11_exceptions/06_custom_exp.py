class OutOfIngredientsError(Exception):
    pass

def make_chai(milk = None, suger = None):
    if milk == None or suger == None:
        raise OutOfIngredientsError("Missing the ingredients...")
    print("Chai is ready")

make_chai()