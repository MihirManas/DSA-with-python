from functools import wraps

def my_decorator(function):
    @wraps(function) #preserves the meta data
    def wrapper():
        print("before function runs")
        function()
        print("after function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello From decorators by Mihir")

greet()
print(greet.__name__)