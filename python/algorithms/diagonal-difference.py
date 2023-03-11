#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    left_diag = 0
    right_diag = 0
    for i in range(len(arr)):
        left_diag += arr[i][i]
        for j in range(len(arr)):
            # or
            # if i == j:
            #     left_diag += arr[i][j]
            if (i + j) == len(arr) - 1:
                print(arr[i][j])
                right_diag += arr[i][j]
                
    return abs(left_diag - right_diag)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
