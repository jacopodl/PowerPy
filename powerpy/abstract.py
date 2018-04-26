class AbstractError(Exception):
    def __init__(self, class_name):
        self.class_name = class_name

    def __str__(self):
        return "abstract class '%s' cannot be instantiated" % self.class_name.__name__


class Abstract(type):
    def __new__(mcs, name, bases, dct):
        dct["__abstract__"] = True
        for base in bases:
            if isinstance(base, Abstract):
                dct["__abstract__"] = False
                break
        return type.__new__(mcs, name, bases, dct)

    def __call__(cls, *args, **kwargs):
        if not getattr(cls, "__abstract__", False):
            return type.__call__(cls, *args, **kwargs)
        raise AbstractError(cls)
