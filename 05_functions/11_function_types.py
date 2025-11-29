def pure_chai(cups):
    return cups * 10

total_chai = 0

#not recomanded
def impure_chai(cups):
    global total_chai
    total_chai += cups * 10

def pour_chai(n):
    if n == 0:
        return "All chai poured"
    print(f"Pouring chai cup {n}")
    return pour_chai(n-1)

print(pour_chai(5))

chai_types = ["light chai", "strong chai", "masala chai", "strong chai"]

strong_chai = list(filter(lambda chai: chai == "strong chai", chai_types))

print(strong_chai)