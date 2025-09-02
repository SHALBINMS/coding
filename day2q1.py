# Question:
# Find the absolute difference between the sum of elements at even indices 
# and the sum of elements at odd indices.

# Optimized solution using slicing

# Test Case 1
arr = [3, 5, 2, 8, 1, 4]  # Expected output: abs((3+2+1) - (5+8+4)) = abs(6 - 17) = 11
n = len(arr)
even_sum = sum(arr[::2])  # picks index 0, 2, 4
odd_sum = sum(arr[1::2])  # picks index 1, 3, 5
s = abs(even_sum - odd_sum)
print(f"Test Case 1 Output: {s}")

# Test Case 2
arr = [10, 20, 30, 40, 50]  # Expected output: abs((10+30+50) - (20+40)) = abs(90 - 60) = 30
n = len(arr)
even_sum = sum(arr[::2])
odd_sum = sum(arr[1::2])
s = abs(even_sum - odd_sum)
print(f"Test Case 2 Output: {s}")

# Test Case 3
arr = [1, 2, 3, 4]  # Expected output: abs((1+3) - (2+4)) = abs(4 - 6) = 2
n = len(arr)
even_sum = sum(arr[::2])
odd_sum = sum(arr[1::2])
s = abs(even_sum - odd_sum)
print(f"Test Case 3 Output: {s}")
