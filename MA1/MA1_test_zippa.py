# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import *


class Test(unittest.TestCase):

    def test_zippa(self):
        print('\nTests zippa')
        l1 = l2 = [1, 2, 3, 4, 5, 6]
        
        self.assertEqual(zippa(l1, l2), [1, 1, 2, 2, 3, 3, 4, 4 ,5 ,5, 6, 6])
        self.assertEqual(zippa(l1[3:], l2[:3]), [4, 1, 5, 2, 6, 3])
        self.assertEqual(zippa(l1, []), [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
