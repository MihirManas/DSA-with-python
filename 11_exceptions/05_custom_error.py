def brew_chai(flavour=None):
    if flavour == None:
        raise TypeError("I think you have forgotten to add the flavour")
    if flavour not in ["masala", "ginger", "elaichi"]:
        raise ValueError("Unsupported Chai...")
    print(f"brewing {flavour} chai...")

brew_chai()