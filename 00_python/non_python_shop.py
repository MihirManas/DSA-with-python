class Chai:
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level
    def sip(self):
        print("siping chai")
    def add_suger(self, amount):
        print("added suger")


my_chai = Chai(sweetness=5, milk_level=3)
my_chai.add_suger(2)