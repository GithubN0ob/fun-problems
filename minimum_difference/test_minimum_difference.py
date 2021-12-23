import unittest
from minimum_difference import min_diff


class TestMinimumDifference(unittest.TestCase):

    def test_min_diff(self):
        print(min_diff([-1, 3, 8, 2, 9, 51], [4, 1, 2, 10, 5, 20], 25))

if __name__ == '__main__':
    unittest.main()
