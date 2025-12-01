class BaseChai:
    def __init__(self, type_):
        self.type = type_
    
    def prepare(self):
        print(f"Preparing {self.type} chai....")

#Inheritance
class MasalaChai(BaseChai):
    def add_spices(self):
        print("adding ginger...")

#composition
class ChaiShop:
    chai_cls = BaseChai #no paranthesis because I need to holds the class itself not creating the object now

    def __init__(self):     #constructor
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices() #calling through object
fancy.chai_cls.add_spices(FancyChaiShop) #calling via class name