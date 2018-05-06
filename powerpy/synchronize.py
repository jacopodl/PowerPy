from threading import Lock


def synchronized(method):
    def wrapper(*args, **kwargs):
        self = args[0]
        if "__sync_mutex__" not in vars(self):
            self.__sync_mutex__ = Lock()
        self.__sync_mutex__.acquire()
        try:
            return method(*args, **kwargs)
        finally:
            self.__sync_mutex__.release()

    return wrapper
