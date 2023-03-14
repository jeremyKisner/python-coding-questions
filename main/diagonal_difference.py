#!/bin/python3

# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    left = 0
    right = 0
    for i in range(len(arr)):
        print(arr[i][i])
        print(arr[i][len(arr)-i-1])
        left += arr[i][i]
        right += arr[i][len(arr)-i-1]
    print("left",left)
    print("right",right)
    return abs(left - right)
    

if __name__ == '__main__':
    arr = [[-1, 1, -7, 8],
          [-10, -8, -5, -2],
          [0, 9, 7, -1],
          [4, 4, -2, 1]]


    result = diagonalDifference(arr)
    print(result)
