from inspect import isfunction


def memoize(func):
    if not isfunction(func):
        raise TypeError("func param must be a function")

    if "__cache__" not in vars(func):
        func.__cache__ = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in func.__cache__:
            func.__cache__[key] = func(*args, **kwargs)
        return func.__cache__[key]

    return wrapper


def clear(func, *args, **kwargs):
    if not isfunction(func):
        raise TypeError("func param must be a function")
    if func.__closure__ is not None:
        for cell in func.__closure__:
            tmp = getattr(cell.cell_contents, "__cache__", None)
            if tmp is not None:
                if args or kwargs:
                    key = (args, tuple(kwargs.items()))
                    del tmp[key]
                else:
                    tmp.clear()
                return
    raise TypeError("func must be a function decorated by @memoize")
