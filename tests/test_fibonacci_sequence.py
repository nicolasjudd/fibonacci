import unittest
from fibonacci import fibonacci_sequence


class test_FibonnaciSequenceFunctionStarts(unittest.TestCase):
    def test_fibonnaciSequenceExists(self):
        self.assertTrue(callable(fibonacci_sequence))
