import unittest
import inspect
from fibonacci import fibonacci_sequence


class test_FibonnaciSequenceFunctionStarts(unittest.TestCase):
    def test_fibonnaciSequenceExists(self):
        self.assertTrue(callable(fibonacci_sequence))

    def test_fibonnaciSequenceReturns(self):
        self.assertTrue(fibonacci_sequence(0) is not None)

    def test_fibonacciSequenceDoesntReturnWithoutSize(self):
        with self.assertRaises(AssertionError):
            fibonacci_sequence(None)
    
    def test_fibonnaciSequenceFunctionReturnsGeneratorForSize(self):
        self.assertTrue(inspect.isgenerator(fibonacci_sequence(0)))

    def test_fibonnaciSequenceFunctionReturnsRightSizeWithOnlySizeArg(self):
        for size in range(100):
            fseq_size = 0
#            with self.subTest(size=size):
            for _ in fibonacci_sequence(size):
                fseq_size += 1
            self.assertEqual(size, fseq_size)

    def test_fibonnaciSequenceFunctionReturnsRightSizeWithSizeandPos(self):
        for size in range(100):
            for pos in range(10):
                fseq_size = 0
#                with self.subTest(size=size, pos=pos):
                for _ in fibonacci_sequence(size,pos):
                    fseq_size += 1
                self.assertEqual(size, fseq_size)
                
    def test_fibonnaciSequenceFunctionReturnsRightSizeWithSizeandStride(self):
        for size in range(100):
            for stride in range(-10,10):
                if stride == 0: continue
                fseq_size = 0
#                with self.subTest(size=size, stride=stride):
                for _ in fibonacci_sequence(size,stride=stride):
                    fseq_size += 1
                self.assertEqual(size, fseq_size)

    def test_fibonnaciSequenceFunctionReturnsRightSizeWithSizePosStride(self):
        for size in range(100):
            for pos in range(10):
                for stride in range(-10,10):
                    if stride == 0: continue
                    fseq_size = 0
#                    with self.subTest(size=size, pos=pos,stride=stride):
                    for _ in fibonacci_sequence(size,pos,stride):
                        fseq_size += 1
                    self.assertEqual(size, fseq_size)
                
