import unittest
from fibonacci import fibonacci

class test_FibonacciFunctionStarts(unittest.TestCase):
    def test_fibonacciFunctionExists(self):
        self.assertTrue(callable(fibonacci))
    
