def serve_chai(flavour):
    try:
        print(f"serving {flavour} chai")
        if flavour.lower() == "unknown":
            raise ValueError("We don't know that flavour")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavour} chai is served")
    finally:
        print("Next customer please..")
    
serve_chai("masala")
serve_chai("unknown")