class Chai:
    tempereture = "hot"
    strength = "Strong"

cutting = Chai()
print(cutting.tempereture)

cutting.tempereture = "Mild"
cutting.cup = "Small"
print(f"Strength of the cutting chai is {cutting.tempereture}")
print(f"Inside class strength is {Chai.tempereture}")

del cutting.tempereture
del cutting.cup
print(f"after deleting tempreture of Chai class is {Chai.tempereture}")
print(f"after deleting cup size of cutting chai is {cutting.cup}")