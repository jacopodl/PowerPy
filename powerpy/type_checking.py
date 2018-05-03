from inspect import isroutine, isclass


def isobject(obj):
    """ Return True if the obj is an instance of class"""
    if not obj:
        return False
    return hasattr(obj, "__dict__") and not isroutine(obj) and not isclass(obj)


class EnsureTypes(object):
    def __setattr__(self, key, value):
        __tperr = "property '%s' requiring type %s but received type %s instead"
        if key in self.__dict__:
            lvalue = getattr(self, key)
            lvalue = self.__get_savedtype(key) if lvalue is None else lvalue
            if lvalue is not None:
                if isclass(lvalue):
                    if value is not None:
                        if not isinstance(value, lvalue):
                            raise TypeError(__tperr % (key, lvalue, type(value)))
                    else:
                        self.__savetype(key, lvalue)
                elif type(lvalue) != type(value):
                    if value is not None or not isobject(lvalue):
                        raise TypeError(__tperr % (key, type(lvalue), type(value)))
                    else:
                        self.__savetype(key, type(lvalue))
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        object.__delattr__(self, item)
        self.__del_savedtype(item)

    def __savetype(self, key, obj):
        type_db = getattr(self, "__saved_types__", dict())
        if key not in type_db:
            type_db[key] = obj
        setattr(self, "__saved_types__", type_db)

    def __get_savedtype(self, key):
        type_db = getattr(self, "__saved_types__", dict())
        return None if key not in type_db else type_db[key]

    def __del_savedtype(self, key):
        type_db = getattr(self, "__saved_types__", dict())
        if key in type_db:
            del type_db[key]
