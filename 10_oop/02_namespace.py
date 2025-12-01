class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)

masala = Chai()
print(f"Masala {masala.origin}")
print(masala.is_hot)

masala.is_hot = False
print(masala.is_hot)
masala.flavor = "Masala"
print(masala.flavor)