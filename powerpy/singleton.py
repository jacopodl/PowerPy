class Singleton(type):
    def __new__(mcs, name, bases, dct):
        ist = type.__new__(mcs, name, bases, dct)
        ist.__instance__ = None
        return ist

    def __call__(cls, *args, **kwargs):
        if cls.__instance__ is None:
            cls.__instance__ = type.__call__(cls, *args, **kwargs)
        return cls.__instance__
