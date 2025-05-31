def two_sum(nums, target):
    num_to_index = {}  # Dictionary to store numbers and their indices

    for i, num in enumerate(nums):  # Loop through the list with index and value
        complement = target - num   # Find the number needed to reach the target

        if complement in num_to_index:  # Check if we already saw the needed number
            return [num_to_index[complement], i]  # Return indices of the pair

        num_to_index[num] = i  # Store the current number and its index

    return []  # Just in case no solution is found (though one is guaranteed)

