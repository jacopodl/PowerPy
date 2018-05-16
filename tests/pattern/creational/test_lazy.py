import time
import unittest

from powerpy.pattern.creational.lazy import lazy


class GonzoProperty:
    def __init__(self):
        self.fib = GonzoProperty.fibR(30)

    def __str__(self):
        return str(self.fib)

    @staticmethod
    def fibR(n):
        if n == 1 or n == 2:
            return 1
        return GonzoProperty.fibR(n - 1) + GonzoProperty.fibR(n - 2)


class Container:
    def __init__(self):
        self.__g1 = None
        self.__g2 = None

    @lazy
    def get_gonzo1(self):
        self.__g1 = GonzoProperty()
        return self.__g1


class TestLazy(unittest.TestCase):
    def test_lazy(self):
        c = Container()
        t1 = time.time()
        x = c.get_gonzo1
        t1 = time.time() - t1
        self.assertEqual(str(x), "832040")
        t2 = time.time()
        _ = c.get_gonzo1
        t2 = time.time() - t2
        self.assertGreater(t1, t2)
