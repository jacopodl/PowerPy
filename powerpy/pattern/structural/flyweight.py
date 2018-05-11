from weakref import WeakValueDictionary

from powerpy.dynamic.memoization import args_serializer


class Flyweight:
    def __init__(self, clazz):
        self.clazz = clazz
        self.ref = WeakValueDictionary()

    def __call__(self, *args, **kwargs):
        key = args_serializer(args, kwargs)
        if key not in self.ref:
            obj = self.clazz(*args, **kwargs)
            self.ref[key] = obj
        return self.ref[key]
