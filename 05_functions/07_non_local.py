def update_order():
    chai_type = "Elaichi"
    print(f"Before kitchen: {chai_type}")

    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"
        print(f"Inside kitchen: {chai_type}")
    kitchen()
    print(f"after kitchen: {chai_type}")

update_order()