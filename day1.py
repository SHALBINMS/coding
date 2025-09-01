# [UST GLOBAL - 2024]
# Problem Statement:
# Given an array of integers. For each pair of adjacent elements, 
# take the first element as length and second as breadth. 
# Find area and perimeter (of rectangle) for each pair:
#   - If area > perimeter, it is a type A couple.
#   - If area < perimeter, it is a type B couple.
#   - If area == perimeter, ignore that pair.
# Return the absolute difference between the number of type A and type B couples.
#
# Input Format:
# Size of the array followed by space-separated integers.
# You are NOT supposed to take any input inside the function.
#
# Output Format:
# Return an integer representing abs(countA - countB).
#
# Sample Input 0:
# 5
# 10 5 20 25 15
# Sample Output 0:
# 4
#
# Sample Input 1:
# 4
# 10 40 30 20
# Sample Output 1:
# 3

#!/bin/python3

import math
import os
import random
import re
import sys

def TYPE_A_B_DIFF(arr):
    n = len(arr)
    A = 0
    B = 0
    for i in range(n - 1):
        area = arr[i] * arr[i + 1]
        peri = 2 * (arr[i] + arr[i + 1])
        if area > peri:
            A += 1
        elif area < peri:
            B += 1
        # if area == peri → ignore
    return abs(A - B)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    L_count = int(input().strip())
    L = list(map(int, input().rstrip().split()))
    diff = TYPE_A_B_DIFF(L)

    fptr.write(str(diff) + '\n')
    fptr.close()
