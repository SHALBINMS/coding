def second_largest(arr):
    # Convert to set to keep only unique values
    unique_vals = set(arr)

    # If less than 2 unique elements, no second largest
    if len(unique_vals) < 2:
        return -1

    # Remove the largest element
    unique_vals.remove(max(unique_vals))

    # Now max of remaining is the 2nd largest
    return max(unique_vals)


# ✅ Test Cases
print(second_largest([10, 20, 4, 20, 10, 8]))  # Output: 10
print(second_largest([7, 7, 7, 7, 7]))          # Output: -1
print(second_largest([5, 1]))                   # Output: 1
print(second_largest([100]))                    # Output: -1
print(second_largest([3, 2, 1, 4]))             # Output: 3
