import unittest
import random
import time
import os
import matplotlib.pyplot as plt

from longest_palindromes import longest_palindromes

class TestLongestPalindromes(unittest.TestCase):

    def test_longest_palindromes(self):
        test_string = ''.join(([chr(random.randrange(ord('a'), ord('a')+26)) for _ in range(30000)]))
        print(f'{"*"*80}\nCase test_string = {test_string}\n')
        print(longest_palindromes(test_string))
    
    def complexity_visualizer(self):
        cwd = os.getcwd()
        number_of_trials = 30
        
        for trial in range(1, number_of_trials+1):
            x_axis = [] # No. of inputs
            y_axis = [] # Time
            
            for n in range(1, 10002, 1000):
                test_string = ''.join(([chr(random.randrange(ord('a'), ord('a')+26)) for _ in range(n)]))
                
                start_time = time.perf_counter()
                longest_palindromes(test_string)
                end_time = time.perf_counter()
                
                x_axis.append(n)
                y_axis.append(end_time-start_time)
            
            plt.title('longest_palindrome() Execution Time vs Input Size Graph')
            plt.xlabel('# of Inputs')
            plt.ylabel('Time (seconds)')

            plt.plot(x_axis, y_axis)

            if not os.path.exists(f'{cwd}/longest_palindromes/media'):
                os.mkdir(f'{cwd}/longest_palindromes/media')

            plt.savefig(f'{cwd}/longest_palindromes/media/foo{trial if trial < number_of_trials else ""}.png')

if __name__ == '__main__':
    unittest.main()