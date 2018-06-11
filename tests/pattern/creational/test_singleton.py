import unittest

from powerpy.pattern.creational.singleton import Singleton, SingletonMeta


@Singleton
class Single1:
    def __init__(self, raw: str = None):
        self.raw = raw


@Singleton
class Single2:
    myprop = "Single2PROP"

    @staticmethod
    def decorate_prop():
        return "***%s***" % Single2.myprop

    def inst_prop(self):
        return Single2.decorate_prop()


class SingleMeta1(metaclass=SingletonMeta):
    def __init__(self, raw: str = None):
        self.raw = raw


class SingleMeta2(metaclass=SingletonMeta):
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

    def test_class_checks(self):
        s1 = Single1()
        s2 = Single2()
        self.assertTrue(isinstance(s1, Single1))
        self.assertFalse(isinstance(s2, Single1))

    def test_statics(self):
        s1 = Single2()
        s1.inst_prop()
        self.assertEqual(s1.inst_prop(), "***%s***" % Single2.myprop)


class TestSingletonMeta(unittest.TestCase):
    def test_singleton_eq(self):
        s1 = SingleMeta1("t1")
        s2 = SingleMeta1("t2")
        self.assertEqual(s1, s2)
        self.assertEqual(s1.raw, s2.raw)

    def test_singleton_nq(self):
        s1 = SingleMeta1()
        s2 = SingleMeta2()
        self.assertNotEqual(s1, s2)
