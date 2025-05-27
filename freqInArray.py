#Find the first non-repeating element in an array.

# Define a function to find the first non-repeating element
def is_firstrepeat(arr):
    
    freq = {}  # Create an empty dictionary to store the frequency of each number
    
    # First loop: Count how many times each number appears
    for num in arr:
        freq[num] = freq.get(num, 0) + 1  # If num is not in dict, start at 0, then add 1
    
    # Second loop: Check each number in the original order
    for num in arr:
        if freq[num] == 1:  # If the number appears only once
            return num  # Return it immediately
    
    return -1  # If all numbers repeat, return -1

# Test array
arr = [7, 3, 5, 3, 4, 5, 7, 8]

# Call the function and print the result
print("1st non repeating element in the array:", is_firstrepeat(arr))

