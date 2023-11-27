def nth_most_rare(nums, n):
    # Count occurrences of each number in the list
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1

    # Sort numbers by their occurrences (rarest to most common)
    sorted_nums = sorted(num_counts.keys(), key=lambda x: num_counts[x])

    # Return the nth rarest term
    if 1 <= n <= len(sorted_nums):
        return sorted_nums[n - 1]
    else:
        return None  # Invalid value of n

# Example usage:
numbers = [5, 4, 5, 4, 5, 4, 4, 5, 3, 3, 3, 2, 2, 1, 5]
n_value = 2

result = nth_most_rare(numbers, n_value)
print(f"The {n_value}th rarest term is: {result}")
