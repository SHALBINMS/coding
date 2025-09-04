# Question: Check whether the given number is an Armstrong Number or not.
# An Armstrong number is a number that is equal to the sum of its digits 
# each raised to the power of the number of digits.
#
# Test Cases:
# Input: 153  
# Explanation: 1^3 + 5^3 + 3^3 = 153 → ARMSTRONG  
# Output: ARMSTRONG
#
# Input: 9474  
# Explanation: 9^4 + 4^4 + 7^4 + 4^4 = 9474 → ARMSTRONG  
# Output: ARMSTRONG
#
# Input: 123  
# Explanation: 1^3 + 2^3 + 3^3 = 36 ≠ 123 → NOT ARMSTRONG  
# Output: NOT ARMSTRONG
#
# Input: -153  
# Negative numbers are not considered Armstrong → NOT ARMSTRONG
# Output: NOT ARMSTRONG

n = int(input())
L = len(str(abs(n)))
num = n
s = 0

if n < 0:
    print("NOT ARMSTRONG")
else:
    while n > 0:
        digit = n % 10
        s += digit ** L
        n = n // 10

    if s == num:
        print("ARMSTRONG")
    else:
        print("NOT ARMSTRONG")
