import unittest

from powerpy.currying import Currying


def test_fun(alfa, beta, gamma):
    return alfa + beta + gamma


class TestCurrying(unittest.TestCase):
    def test_Currying(self):
        c_test = Currying(test_fun)
        c1 = c_test("Hello")
        c2 = c1("World")
        self.assertEqual("HelloWorld!", c2("!"))
        self.assertEqual("Hello!World", c1("!", "World"))
        self.assertEqual("!WorldHello", c_test("!", "World", "Hello"))
