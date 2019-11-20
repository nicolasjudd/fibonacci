import unittest
import inspect
from fibonacci import fibonacci

class test_FibonacciFunctionStarts(unittest.TestCase):
    def test_fibonacciFunctionExists(self):
        self.assertTrue(callable(fibonacci))
    
    def test_fibonacciDoesntRunWithNoArguments(self):
        with self.assertRaises(TypeError):
            fibonacci()

    def test_fibonacciDoesntRunWithTooManyRightTypeArguments(self):
        for i in range(3,12):
            with self.subTest(i=i) and self.assertRaises(TypeError):
                fibonacci(*[x for x in range(i)])
    
    def test_fibonacciDoesntRunWithOneFloatArguments(self):
        with self.assertRaises(TypeError):
            fibonacci(1123,58.13)
        
        with self.assertRaises(TypeError):
            fibonacci(11.23,5813)

    def test_fibonacciDoesntRunWithTwoFloatArguments(self):
        with self.assertRaises(TypeError):
            fibonacci(11.23,58.13)

    def test_fibonacciDoesntRunWithTupleArgument(self):
        with self.assertRaises(TypeError):
            fibonacci((1123,5813))

    def test_fibonacciDoesntRunWithListArgument(self):
        with self.assertRaises(TypeError):
            fibonacci([1123,5813])

class test_FibonacciFunctionRuns(unittest.TestCase):
    pass
