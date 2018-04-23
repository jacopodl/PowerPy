import unittest

from powerpy.final import Final, FinalError


class A(metaclass=Final):
    pass


class TestSingleton(unittest.TestCase):
    def test_final(self):
        with self.assertRaises(FinalError):
            BClass = type("B", (A,), {})
