from threading import RLock


def synchronized(method):
    def wrapper(self, *args, **kwargs):
        if "__sync_mutex__" not in vars(self):
            self.__sync_mutex__ = RLock()
        self.__sync_mutex__.acquire()
        try:
            return method(self, *args, **kwargs)
        finally:
            self.__sync_mutex__.release()

    return wrapper


def synchronize_ensure(self):
    self.__sync_mutex__.acquire()


def synchronize_release(self):
    self.__sync_mutex__.release()
