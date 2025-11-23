seat = input("Enter seat type (sleeper/AC/general/luxury): \n").lower()
match seat:
    case "sleeper":
        print("In sleeper you don't have ac but bed.")
    case "ac":
        print("In ac you have ac as well as bed.")
    case "general":
        print("In general you don't have ac or bed. cheap price but no reservation.")
    case "luxury":
        print("In luxury you have ac, bed, and extra legroom.")
    case _:
        print("Invalid seat type entered.")