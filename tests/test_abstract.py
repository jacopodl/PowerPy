import unittest

from powerpy.abstract import Abstract, AbstractError


class A(metaclass=Abstract):
    pass


class B(A):
    pass


class TestSingleton(unittest.TestCase):
    def test_abstract_fail(self):
        with self.assertRaises(AbstractError):
            A()

    def test_abstract_success(self):
        b = B()
        self.assertIsInstance(b, B)
