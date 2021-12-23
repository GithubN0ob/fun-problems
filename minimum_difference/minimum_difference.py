import math

'''
Problem description:

Source: https://www.youtube.com/watch?v=GBuHSRDGZBY

Solution time complexity: O(n^2)
space complexity: O(n)

Notes:
There are more efficient approaches.
'''

def min_diff(a, b, target):
    minimum_diff = math.inf
    sol = None
    for p in a:
        for q in b:
            diff = abs(target - (p+q))
            if diff < minimum_diff:
                sol = p, q
                minimum_diff = diff
    return sol