import time
import unittest

from powerpy.dynamic.memoization import memoize, clear


@memoize
def simple(value, string):
    return string * value


class TestMemoization(unittest.TestCase):
    def test_memoize(self):
        t1 = time.time()
        simple(24242424, "test_this_memo")
        simple(24242424, "test")
        simple(123, "this")
        simple(2018, "memo")
        t1 = time.time() - t1
        t2 = time.time()
        simple(24242424, "test_this_memo")
        simple(24242424, "test")
        simple(123, "this")
        simple(2018, "memo")
        t2 = time.time() - t2
        self.assertGreater(t1, t2)

    def test_clear(self):
        simple(2, "test_this_memo")
        self.assertTrue(simple.__closure__[0].cell_contents.__cache__)
        clear(simple)
        self.assertFalse(simple.__closure__[0].cell_contents.__cache__)
        simple(24, "J")
        simple(27, "A")
        self.assertEqual(simple.__closure__[0].cell_contents.__cache__["24J"], "J" * 24)
        self.assertEqual(simple.__closure__[0].cell_contents.__cache__["27A"], "A" * 27)
        clear(simple, 27, "A")
        self.assertEqual(simple.__closure__[0].cell_contents.__cache__["24J"], "J" * 24)
        with self.assertRaises(KeyError):
            _ = simple.__closure__[0].cell_contents.__cache__["27a"]
