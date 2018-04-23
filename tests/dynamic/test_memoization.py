import time
import unittest

from powerpy.dynamic.memoization import memoization


@memoization
def simple(value, string):
    return string * value


class TestMemoization(unittest.TestCase):
    def test_memoization(self):
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
