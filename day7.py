"""
📌 Problem Statement:
Given an integer N, generate an N × N matrix such that 
the element at position (row, col) = row + col + 1.
Finally, print the matrix.

⚡ Constraints:
2 <= N <= 20

✅ Sample Test Case 1:
Input:
3

Output:
1 2 3
2 3 4
3 4 5

✅ Sample Test Case 2:
Input:
4

Output:
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
"""

matx = []
n = int(input("Enter matrix size: "))

# Initialize matrix with zeros
for i in range(n):
    matx.append([0] * n)
    
# Fill the matrix using row + col + 1 formula
for row in range(n):
    for col in range(n):
        matx[row][col] = row + col + 1
        
# Print the matrix
for row in range(n): 
    print()
    for col in range(n):
        print(matx[row][col], end=" ")
