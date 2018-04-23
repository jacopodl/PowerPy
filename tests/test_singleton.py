import unittest

from powerpy.singleton import Singleton


class Single1(metaclass=Singleton):
    def __init__(self, raw: str = None):
        self.raw = raw


class Single2(metaclass=Singleton):
    pass


class TestSingleton(unittest.TestCase):
    def test_singleton_eq(self):
        s1 = Single1("t1")
        s2 = Single1("t2")
        self.assertEqual(s1, s2)
        self.assertEqual(s1.raw, s2.raw)

    def test_singleton_nq(self):
        s1 = Single1()
        s2 = Single2()
        self.assertNotEqual(s1, s2)
