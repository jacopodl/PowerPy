from powerpy.synchronize import synchronized, synchronize_ensure, synchronize_release


class Observer:
    def update(self, *args, **kwargs):
        pass


class Observable:
    def __init__(self):
        self.observers = []
        self.changed = False

    @synchronized
    def add_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    @synchronized
    def del_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    @property
    def has_changed(self):
        return self.changed

    def set_changed(self):
        self.changed = True

    def notify_observers(self, *args, **kwargs):
        try:
            synchronize_ensure(self)
            if not self.changed:
                return
            alocal = self.observers
            self.changed = False
        finally:
            synchronize_release(self)

        for obs in alocal:
            obs.update(*args, **kwargs)
