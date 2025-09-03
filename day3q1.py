"""
**Question: Maximum Difference in Array**

Given an array of integers, find the **maximum value of arr[j] - arr[i] such that j > i**.

**Input Format:**
* First line: integer `n` (size of array, n ≤ 100)
* Second line: n integers (array elements, can be positive or negative)

**Output Format:**
* Single integer: maximum difference

**Constraint:** j > i (j must come after i in the array)

**Sample Test Cases:**

Example 1:
Input:
6
2 3 10 6 4 8
Output: 8
Explanation: Maximum difference = arr[2] - arr[0] = 10 - 2 = 8

Example 2:
Input:
5
7 9 5 6 3
Output: 2
Explanation: Maximum difference = arr[1] - arr[0] = 9 - 7 = 2

Example 3:
Input:
4
10 8 6 2
Output: -2
Explanation: Array is decreasing, so maximum difference = arr[1] - arr[0] = 8 - 10 = -2
"""

# SOLUTION
n = int(input())
arr = list(map(int, input().split()))
n = len(arr)
max_diff = float('-inf')
for i in range(n):
    for j in range(i+1, n):
        diff = arr[j] - arr[i]
        if diff > max_diff:
            max_diff = diff
print(max_diff)

"""
**Additional Test Cases for Comprehensive Testing:**

Test Case 4 - Two elements (positive):
Input:
2
5 10
Output: 5

Test Case 5 - Two elements (negative):
Input:
2
15 3
Output: -12

Test Case 6 - All same elements:
Input:
4
7 7 7 7
Output: 0

Test Case 7 - Strictly increasing:
Input:
5
1 2 3 4 5
Output: 4

Test Case 8 - Single large jump:
Input:
6
1 1 1 100 1 1
Output: 99

Test Case 9 - All negative numbers:
Input:
4
-5 -2 -8 -1
Output: 3

Test Case 10 - Mixed positive/negative:
Input:
5
-3 5 -1 8 -2
Output: 11

Test Case 11 - Large numbers:
Input:
3
1000000 999999 1000001
Output: 1

Test Case 12 - Maximum element at end:
Input:
5
5 3 1 2 10
Output: 5

Test Case 13 - Including zero:
Input:
5
0 -5 10 -3 7
Output: 15

Test Case 14 - Peak in middle:
Input:
5
1 5 2 8 3
Output: 7

Test Case 15 - Complex arrangement:
Input:
8
3 1 4 1 5 9 2 6
Output: 8

**Edge Cases Covered:**
✅ Minimum array size (n=2)
✅ All elements same
✅ Strictly increasing/decreasing arrays
✅ Negative numbers
✅ Mixed positive/negative
✅ Large numbers
✅ Zero included
✅ Maximum difference at different positions

**Time Complexity:** O(n²)
**Space Complexity:** O(1)
**Constraints:** Works for n ≤ 100 as specified
"""