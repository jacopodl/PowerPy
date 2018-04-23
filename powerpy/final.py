class FinalError(Exception):
    def __init__(self, class_name):
        self.class_name = class_name

    def __str__(self):
        return "class %s is final" % self.class_name.__name__


class Final(type):
    def __init__(cls, name, bases, dct):
        type.__init__(cls, name, bases, dct)
        for base in bases:
            if isinstance(base, Final):
                raise FinalError(base)
