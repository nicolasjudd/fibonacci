import unittest
from fibonacci import fibonacci_pos


class test_FibonacciFunctionStarts(unittest.TestCase):
    def test_fibonacci_posFunctionExists(self):
        self.assertTrue(callable(fibonacci_pos))

    def test_fibonacci_posDoesntRunWithNoArguments(self):
        with self.assertRaises(TypeError):
            fibonacci_pos()

    def test_fibonacci_posDoesntRunWithTooManyRightTypeArguments(self):
        for i in range(2, 12):
            with self.subTest(i=i) and self.assertRaises(TypeError):
                fibonacci_pos(*[x for x in range(i)])

    def test_fibonacci_posDoesntRunWithNegativeArgument(self):
        with self.assertRaises(AssertionError):
            fibonacci_pos(-1)

    def test_fibonacci_posDoesntRunWithOneFloat(self):
        with self.assertRaises(AssertionError):
            fibonacci_pos(58.13)

    def test_fibonacci_posDoesntRunWithTupleArgument(self):
        with self.assertRaises(AssertionError):
            fibonacci_pos((1123, 5813))

    def test_fibonacci_posDoesntRunWithListArgument(self):
        with self.assertRaises(AssertionError):
            fibonacci_pos([1123, 5813])


class test_FibonacciFunctionRuns(unittest.TestCase):
    def test_fibonacciReturnsCorrectValuesinSequence(self):
        for i, val in enumerate([0,1,1,2,3,5,8,13,21,34,55,89,144,233,377]):
            with self.subTest(pos=i):
                self.assertEqual(fibonacci_pos(i),val)
