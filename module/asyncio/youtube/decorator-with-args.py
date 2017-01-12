from functools import wraps

def debug(prefix=''):
    def decorator(func):
        msg = prefix + func.__qualname__
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(msg)
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Usage
# @debug(prefix='***')
# def add(x,y):
#       return x + y
