# [UST GLOBAL - 2024]
# Problem Statement:
# Given a string, you are supposed to write a code for returning its score.
# For each palindrome substring of length 4, add 5 to the score.
# For each palindrome substring of length 5, add 10 to the score.
# Palindrome checking is case sensitive.
# Score is initialized to 0.
#
# Input Format:
# A single string input is provided as the first line.
# This input is already passed as a parameter to the function.
# You are NOT supposed to take input inside the function.
#
# Constraints:
# NA
#
# Output Format:
# Return the final score as an integer.
#
# Sample Input 0:
# ABCBAAAA
# Sample Output 0:
# 15
#
# Sample Input 1:
# ABABAABBA
# Sample Output 1:
# 20

#!/bin/python3

import math
import os
import random
import re
import sys

def PALINDROME_SCORE(inp_str):
    score = 0
    n = len(inp_str)
    
    for i in range(n - 4 + 1):
        if inp_str[i:i+4] == inp_str[i:i+4][::-1]:
            score += 5
    for i in range(n - 5 + 1):
        if inp_str[i:i+5] == inp_str[i:i+5][::-1]:
            score += 10
    return score

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    inp_str = input()
    score = PALINDROME_SCORE(inp_str)
    fptr.write(str(score) + '\n')
    fptr.close()
