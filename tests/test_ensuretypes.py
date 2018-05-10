import unittest

from powerpy.type_checking import EnsureTypes


class Ext:
    pass


class T1(EnsureTypes):
    def __init__(self):
        self.generic = None
        self.string = ""
        self.num = 12
        self.clazz = Ext
        self.instance = Ext()


class TestEnsureTypes(unittest.TestCase):
    def test_basetype(self):
        test = T1()
        with self.assertRaises(TypeError):
            test.string = 22
        test.string = "Hello"

    def test_generic(self):
        test = T1()
        test.generic = "Hello"
        test.generic = 123

    def test_newprop(self):
        test = T1()
        test.newprop = None
        test.newprop = ""
        test.newprop = 22

    def test_clazz_and_obj(self):
        test = T1()
        test.clazz = None
        with self.assertRaises(TypeError):
            test.clazz = "TEST"
        test.clazz = Ext()
        test.instance = None
        test.instance = test.clazz
