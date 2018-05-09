import unittest

from powerpy.pattern.observable import Observer, Observable


class Manager(Observable):
    def __init__(self):
        Observable.__init__(self)
        self.prop = 0

    def change_and_notify(self):
        self.prop += 1
        self.set_changed()
        self.notify_observers(self.prop)


class Observer1(Observer):
    def __init__(self):
        Observer.__init__(self)
        self.count = 100

    def update(self, item):
        self.count += item


class TestObservable(unittest.TestCase):
    def test_observer(self):
        m = Manager()
        o = Observer1()
        m.add_observer(o)
        self.assertEqual(o.count, 100)
        b = o.count
        for i in range(10):
            m.change_and_notify()
            b += i + 1
        self.assertEqual(o.count, b)
        # without set changed
        m.notify_observers(100)
        self.assertEqual(o.count, b)
        # with set changed
        m.set_changed()
        m.notify_observers(100)
        self.assertEqual(o.count, b + 100)

    def test_add_del(self):
        m = Manager()
        o = Observer1()
        self.assertEqual(m.observers, [])
        m.add_observer(o)
        self.assertEqual(m.observers, [o])
        m.add_observer(o)
        self.assertEqual(m.observers, [o])
        m.del_observer(o)
        self.assertEqual(m.observers, [])
        self.assertEqual(m.observers, [])
