import unittest
from fibonacci import fibonacci_nearest

class test_FibonacciNearestFunctionStarts(unittest.TestCase):
    def test_fibonacci_nearestFunctionExists(self):
        self.assertTrue(callable(fibonacci_nearest))

    def test_fibonacci_nearestDoesntRunWithTupleArgument(self):
        with self.assertRaises(AssertionError):
            fibonacci_nearest((1123, 5813))

    def test_fibonacci_nearestDoesntRunWithListArgument(self):
        with self.assertRaises(AssertionError):
            fibonacci_nearest([1123, 5813])

class test_FibonacciNearestFunctionRuns(unittest.TestCase):
    def test_fibonacci_nearestLowerReturnsLowerNumber(self):
        self.assertEqual(fibonacci_nearest(7,kind="lower"),5)

    def test_fibonacci_nearestUpperReturnsLowerNumber(self):
        self.assertEqual(fibonacci_nearest(6,kind="upper"),8)

    def test_fibonacci_nearestNearestReturnsNearestNumber(self):
        self.assertEqual(fibonacci_nearest(6,kind="nearest"),5)
        self.assertEqual(fibonacci_nearest(7,kind="nearest"),8)

    def test_fibonacci_nearestNearestReturnsUpperIfEquidistant(self):
        self.assertEqual(fibonacci_nearest(4,kind="nearest"),5)

