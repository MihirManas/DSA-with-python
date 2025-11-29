chai_type = "Plain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Kashmiri"
        print(f"Inside kitchen: {chai_type}")
    kitchen()

front_desk()
print(f"Final Global Chai: {chai_type}")