from functools import wraps

def require_admin(function):
    def wrapper(user):
        if user != "admin":
            print("no access ! admin only")
            return 0
        else:
            return(function(user))
    return wrapper

@require_admin
def chai_invertory(role):
    print("Hii Boss kese ana hua ?")

chai_invertory("Kodi")
chai_invertory("admin")