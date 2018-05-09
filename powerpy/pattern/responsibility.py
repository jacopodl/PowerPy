class Handler:
    def __init__(self):
        self.next = None

    def set_next(self, handler):
        if self.next is None:
            self.next = handler
        else:
            self.next.set_next(handler)
        return self

    def next_handler(self, *args, **kwargs):
        if self.next is not None:
            return self.next.handle(*args, **kwargs)
        return None

    def handle(self, *args, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def forward_if(retval=None):
        def wr_method(method):
            def wrapper(self, *args, **kwargs):
                val = method(self, *args, **kwargs)
                if val == retval:
                    return self.next_handler(*args, **kwargs)
                return val

            return wrapper

        return wr_method
