from inspect import isfunction, isroutine, isclass


def args_serializer(*args, **kwargs):
    def _serialize(arg):
        tmp = str()
        if type(arg) == list or type(arg) == tuple:
            for itm in arg:
                tmp += _serialize(itm)
            return tmp
        elif type(arg) == dict:
            for k, v in arg.items():
                tmp += _serialize(k) + _serialize(v)
            return tmp
        elif hasattr(arg, "__dict__") and not isroutine(arg) and not isclass(arg):
            return _serialize(arg.__dict__)
        return str(arg)

    rt = _serialize(args)
    if kwargs:
        rt += _serialize(kwargs)
    return rt


def memoize(func):
    if not isfunction(func):
        raise TypeError("func param must be a function")

    if "__cache__" not in vars(func):
        func.__cache__ = {}

    def wrapper(*args, **kwargs):
        key = args_serializer(args, kwargs)
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
                    key = args_serializer(args, kwargs)
                    del tmp[key]
                else:
                    tmp.clear()
                return
    raise TypeError("func must be a function decorated by @memoize")
