#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    result = {}
    result["total"] = 0
    result["positive"] = 0
    result["zero"] = 0
    result["negative"] = 0
    for item in arr:
        result["total"] += 1
        if item == 0:
            result["zero"] += 1
        if item > 0:
            result["positive"] += 1
        if item < 0:
            result["negative"] += 1
    print(f"{float(result['positive'] / result['total']):.6f}") 
    print(f"{float(result['negative'] / result['total']):.6f}") 
    print(f"{float(result['zero'] / result['total']):.6f}") 


if __name__ == '__main__':
    arr = [-4, 3, -9, 0, 4, 1]
    plusMinus(arr)
