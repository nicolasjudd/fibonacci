import unittest
from fibonacci import fibonacci

class test_FibonacciFunctionExists(unittest.TestCase):
    def test_fibonacci_function_exists(self):
        self.assertTrue(callable(fibonacci))
