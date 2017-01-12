from functools import wraps, partial

def debug(func=None, *, prefix=''):
    if func is None:
        return partial(debug, prefix=prefix)

    msg = prefix + func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper

