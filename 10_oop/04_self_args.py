class ChaiCup:
    size = 150 #ml

    def describe(self):
        return f"A {self.size}ml cup chai cup.\n"
    
cup = ChaiCup()
print(cup.describe())
print(ChaiCup.describe(ChaiCup))

cup_two = ChaiCup()
cup_two.size = 100
print(ChaiCup.describe(cup_two))