from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **keywords):
        print(f"calling: {func.__name__}")
        result = func(*args, **keywords)
        print(f"finished: {func.__name__}")
        return result
    return wrapper

@log_activity
def brew_chai(type, milk = "No"):
    print(f"brewing {type} chai with {milk} milk")

brew_chai("Masala")