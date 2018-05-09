from threading import RLock


def __mkmutex(obj):
    if "__sync_mutex__" not in vars(obj):
        obj.__sync_mutex__ = RLock()


def synchronized(method):
    def wrapper(self, *args, **kwargs):
        __mkmutex(self)
        self.__sync_mutex__.acquire()
        try:
            return method(self, *args, **kwargs)
        finally:
            self.__sync_mutex__.release()

    return wrapper


def synchronize_ensure(self):
    __mkmutex(self)
    self.__sync_mutex__.acquire()


def synchronize_release(self):
    self.__sync_mutex__.release()
