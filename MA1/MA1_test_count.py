# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import *

lst = [1, 2, 3, 4, 5, [1, 2, 3, 4, 5, [1, 2, 3, 4, 5], 1, 2, 3, 4, 5], 1, 2, 3, 4, 5]

class Test(unittest.TestCase):

    def test_count(self):
        print('\nTests count')
        self.assertEqual(count(2, lst), 5)
        self.assertEqual(count(2, lst[5]), 3)
        self.assertEqual(count(2, lst[:6]), 4)
        self.assertEqual(count(2, lst[6:]), 1)


if __name__ == "__main__":
    unittest.main()
