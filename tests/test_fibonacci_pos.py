import unittest
import random
from fibonacci import fibonacci_pos

LOAD_RUNS = 2000

class test_FibonacciPosFunctionStarts(unittest.TestCase):
    def test_fibonacci_posFunctionExists(self):
        self.assertTrue(callable(fibonacci_pos))

    def test_fibonacci_posDoesntRunWithNoArguments(self):
        with self.assertRaises(TypeError):
            fibonacci_pos()

    def test_fibonacci_posDoesntRunWithTooManyRightTypeArguments(self):
        for pos in range(2, 12):
            with self.subTest(pos=pos) and self.assertRaises(TypeError):
                fibonacci_pos(*[x for x in range(pos)])

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


class test_FibonacciPosFunctionRuns(unittest.TestCase):
    def test_fibonacciReturnsCorrectValuesinSequence(self):
        for i, val in enumerate([0,1,1,2,3,5,8,13,21,34,55,89,144,233,377]):
            with self.subTest(pos=i):
                self.assertEqual(fibonacci_pos(i),val)

    def test_fibonacciPosReturnsCorrectValuesOutOfSequence(self):
        for pos, val in [(10,55),(2,1),(12,144),(14,377),(0,0)]:
            with self.subTest(pos=pos, val=val):
                self.assertEqual(fibonacci_pos(pos),val)

    def test_fibonacciPosReturnsUnderLoad(self):
        for pos in range(LOAD_RUNS):
            with self.subTest(pos=pos):
                try:
                    fibonacci_pos(pos)
                except:
                    self.assertTrue(False)
                    return
        self.assertTrue(True)

    def test_fibonacciPosReturnsUnderLoadBackward(self):
        for pos in range(LOAD_RUNS,0,-1):
            with self.subTest(pos=pos):
                try:
                    fibonacci_pos(pos)
                except:
                    self.assertTrue(False)
                    return
        self.assertTrue(True)

    def test_fibonacciPosReturnsUnderRandomOrderLoad(self):
        for _ in range(LOAD_RUNS):
            try:
                pos = random.randint(0,LOAD_RUNS) 
                fibonacci_pos(pos)
            except:
                self.assertTrue(False)
                return
        self.assertTrue(True)
