#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def balancedSums(arr):
    # Write your code here
    # arr = [0] + arr
    # arr.append(0)
    if len(arr) == 1:
        return "YES"
    sum_all = sum(arr)
    sum_left = 0
    for i in range(len(arr)):
        # sum_left = sum(arr[:i])
        sum_right = sum_all - sum_left - arr[i]
        if sum_left == sum_right:
            return "YES"
        sum_left += arr[i]
    return "NO"


print(balancedSums())
