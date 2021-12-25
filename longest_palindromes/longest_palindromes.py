'''
Problem description:

Source: https://www.youtube.com/watch?v=0CKUjDcUYYA&t=8s

Solution time complexity: O(nlogn)
space complexity: O(nlogn)

Notes:
This is just a brute force method. There are more efficient approaches.
'''

def check_around(string, leftindex, rightindex):
    # abccba
    # abcba
    return_string = '' if rightindex - leftindex == 1 else string[(leftindex+rightindex)//2]
    for x in range(min(leftindex +1, len(string) - rightindex)):
        left_pointer = leftindex - x
        right_pointer = rightindex + x
        if left_pointer < 0 or right_pointer >= len(string) or string[left_pointer] != string[right_pointer]:
            break
        return_string = string[left_pointer] + return_string + string[right_pointer]
    return return_string

def longest_palindromes(string):
    if string == None:
        return ''
    longest = 0
    candidates = []
    # abccba
    # abcba
    for index in range(len(string)):   
        if index+2 < len(string):
            result1 = check_around(string, index, index+2) # abcba
            if not len(result1) < longest:
                longest, candidates = (len(result1), [result1]) if len(result1) > longest else (longest, candidates+[result1])

            result2 = check_around(string, index, index+1) #abba
            if not len(result2) < longest:
                longest, candidates = (len(result2), [result2]) if len(result2) > longest else (longest, candidates+[result2])
        else:
            if index+1 < len(string):
                result2 = check_around(string, index, index+1) #abba
                if not len(result2) < longest:
                    longest, candidates = (len(result2), [result2]) if len(result2) > longest else (longest, candidates+[result2])
    return candidates, longest