def make_chai():
    return "Here is your masala chai"

print(make_chai())

def idli_chaiwala():
    pass

print(idli_chaiwala())

def sold_cups():
    return 120

total = sold_cups()
print(total)

def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry chai is over"
    return "Chai is available"

print(chai_status(0))
print(chai_status(5))

def chai_report():
    return 100, 20 #sold, left

sold, _ = chai_report()
print("Sold:", sold)