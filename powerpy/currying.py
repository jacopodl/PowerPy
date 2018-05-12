class Currying(object):
    def __init__(self, fun):
        self.fun = fun
        self.argc = fun.__code__.co_argcount
        self.argl = ()

    def __call__(self, *args):
        tmp = self.argl + args
        if len(tmp) >= self.argc:
            return self.fun(*tmp)
        curr = Currying(self.fun)
        curr.argl = tmp
        return curr


def uncurrying(obj):
    if not isinstance(obj, Currying):
        raise TypeError("obj must be a function decorated with @Currying")
    return obj.fun
