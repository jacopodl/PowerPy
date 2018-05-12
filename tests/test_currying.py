import types
import unittest

from powerpy.currying import Currying, uncurrying


@Currying
def test_fun(alfa, beta, gamma):
    return alfa + beta + gamma


class TestCurrying(unittest.TestCase):
    def test_Currying(self):
        c1 = test_fun("Hello")
        c2 = c1("World")
        self.assertEqual("HelloWorld!", c2("!"))
        self.assertEqual("Hello!World", c1("!", "World"))
        self.assertEqual("!WorldHello", test_fun("!", "World", "Hello"))

    def test_uncurrying(self):
        func = uncurrying(test_fun)
        self.assertEqual(type(func), types.FunctionType)
        with self.assertRaises(TypeError):
            uncurrying(func)
