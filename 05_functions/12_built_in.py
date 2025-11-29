def chai_flavour(flavour = "masala"):
    """return the flavour of chai"""
    return f"This is a cup of {flavour} chai."

print(chai_flavour.__doc__)
print(chai_flavour.__name__)

def generate_bill(chai = 0, samosa = 0):
    """
    calculate the total bill for chai and samosa

    :param chai: number of chai cups (10 rupees each)
    :param samosa: number of samosas (20 rupees each)
    :return: (total amount, thank you message)
    """
    total = chai * 10 + samosa * 20
    return total, "Thank you for your order!"