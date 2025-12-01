class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size
    
    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"]
        )
    
    @classmethod
    def from_string(cls, order_data):
        tea_type, sweetness, size = order_data.split(",")
        return(cls(tea_type, sweetness, size))
    
class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]
print(ChaiUtils.is_valid_size("Medium"))

order_1 = ChaiOrder.from_dict({"tea_type": "Ragular", "sweetness": "Medium", "size": "Large"})
order_2 = ChaiOrder.from_string(input("what type of chai you want ? put it along with sweetness and size\n"))

print(order_1.__dict__)
print(order_2.__dict__)