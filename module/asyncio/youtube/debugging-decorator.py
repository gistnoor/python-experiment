from functools import wraps

def debug(func):
    msg = func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        print(func.__name__)
        return func(*args, **kwargs)
    return wrapper

# Application wrapping
func = debug(func)
