import unittest
import random
from longest_palindromes import longest_palindromes

class TestLongestPalindromes(unittest.TestCase):

    def test_longest_palindromes(self):
        test_string = ''.join(([chr(random.randrange(ord('a'), ord('a')+26)) for _ in range(30000)]))
        print(f'{"*"*80}\nCase test_string = {test_string}\n')
        print(longest_palindromes(test_string))

if __name__ == '__main__':
    unittest.main()