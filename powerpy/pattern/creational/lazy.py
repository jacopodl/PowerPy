def lazy(func):
    fnattr = "__lazy_" + func.__name__

    @property
    def wrapper(*args, **kwargs):
        if not hasattr(func, fnattr):
            setattr(func, fnattr, func(*args, **kwargs))
        return getattr(func, fnattr)

    return wrapper
