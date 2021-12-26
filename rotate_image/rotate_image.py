'''
Rotate image clockwise
'''

def rotate_image(array2d):
    if array2d == None:
        return []
    return [[array2d[len(array2d)-1 -x][col_index] for x in range(len(array2d))] for col_index in range(len(array2d[0]))]

test = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print('\n'.join(str(array) for array in rotate_image(test)))