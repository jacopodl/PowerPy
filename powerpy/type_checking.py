from inspect import isroutine, isclass


def isobject(obj):
    """ Return True if the obj is an instance of class"""
    if not obj:
        return False
    return hasattr(obj, "__dict__") and not isroutine(obj) and not isclass(obj)


class EnsureTypes(object):
    def __setattr__(self, key, rvalue):
        if key in self.__dict__:
            lvalue = self.__get_savedtype(key)
            if lvalue is None:
                self.__savetype(key, None)
            else:
                if isclass(lvalue):
                    if rvalue is not None:
                        if not isinstance(rvalue, lvalue):
                            raise TypeError("property '%s' required instance of class '%s' but received type %s " %
                                            (key, lvalue.__qualname__, type(rvalue)))
                    else:
                        self.__savetype(key, lvalue)
                elif type(lvalue) != type(rvalue):
                    if rvalue is not None or not isobject(lvalue):
                        raise TypeError("property '%s' required type '%s' but received type %s " %
                                        (key, type(lvalue), type(rvalue)))
                    else:
                        self.__savetype(key, type(lvalue))
        object.__setattr__(self, key, rvalue)

    def __delattr__(self, item):
        object.__delattr__(self, item)
        self.__del_savedtype(item)

    def __savetype(self, key, obj):
        type_db = getattr(self, "__saved_types__", dict())
        if key not in type_db:
            type_db[key] = obj
            object.__setattr__(self, "__saved_types__", type_db)

    def __get_savedtype(self, key):
        type_db = getattr(self, "__saved_types__", dict())
        return getattr(self, key) if key not in type_db else type_db[key]

    def __del_savedtype(self, key):
        type_db = getattr(self, "__saved_types__", dict())
        if key in type_db:
            del type_db[key]
