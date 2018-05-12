import gc
import unittest

from powerpy.pattern.structural.flyweight import Flyweight


@Flyweight
class Point:
    def __init__(self, x, y, z):
        object.__setattr__(self, "x", x)
        object.__setattr__(self, "y", y)
        object.__setattr__(self, "z", z)

    def __setattr__(self, key, value):
        # Make Point immutable
        pass


class TestFlyweight(unittest.TestCase):
    def test_flyweight(self):
        p1 = Point(1, 2, 3)
        p2 = Point(4, 3, 7)
        p3 = Point(1, 2, 3)
        self.assertEqual(p1 is p3, True)
        self.assertEqual(p1 is p2, False)
        p2 = id(p2)
        gc.collect()
        p22 = Point(4, 3, 7)
        self.assertEqual(p2 == id(p22), False)
