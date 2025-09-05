import math
import os
import sys

# ❓ Problem Statement:
# Given an array of integers, find the LCM between the adjacent pairs in the array
# and add these LCMs into a set. Return the largest element from the set.
#
# 📌 Input Format:
#   First line: Size of the array (N)
#   Second line: N space-separated integers
#
# 📌 Output Format:
#   A single integer (largest LCM)
#
# 🔹 Formula Used:
#   LCM(a, b) = (a * b) // gcd(a, b)
#
# 🧪 Sample Test Cases:
# Input 0:
# 5
# 10 5 25 33 77
# Output 0:
# 825
#
# Input 1:
# 7
# 10 20 30 40 50 60 70
# Output 1:
# 420
#
# Input 2:
# 4
# 2 3 4 5
# Output 2:
# 20
#
# Input 3:
# 6
# 6 12 18 24 30 36
# Output 3:
# 180

def LARGEST_LCM(arr):
    lcm_set = set()  # To store unique LCM values
    for i in range(len(arr) - 1):  # Loop through adjacent pairs
        a, b = arr[i], arr[i + 1]
        lcm_val = (a * b) // math.gcd(a, b)  # Formula for LCM
        lcm_set.add(lcm_val)
    return max(lcm_set)  # Return largest LCM

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Input handling
    L_count = int(input().strip())
    L = list(map(int, input().rstrip().split()))

    # Call function
    lar = LARGEST_LCM(L)

    # Output result
    fptr.write(str(lar) + '\n')
    fptr.close()
