def add_vat(price, vat):
    return price + (price * vat / 100)

orders = [100, 200, 300]

for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Final amount including VAT: {final_amount}")

def print():
    print("I have printed a message")

print()