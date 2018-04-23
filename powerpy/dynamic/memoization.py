def memoization(f):
    if '__cache__' not in vars(f):
        f.__cache__ = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in f.__cache__:
            f.__cache__[key] = f(*args, **kwargs)
        return f.__cache__[key]

    return wrapper
