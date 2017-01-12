from functools import wraps
import logging

def debug(func):
    log = logging.getLogger(func.__module__)
    msg = func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.debug(msg)
        return func(*args, **kwargs)
    return wrapper
