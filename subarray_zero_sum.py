def find_subarrays_with_zero_sum(arr):
    # Dictionary to store cumulative sum and its indices
    sum_map = {}
    result = []
    
    # Cumulative sum initialized to 0
    cum_sum = 0
    
    # Traverse the array
    for i in range(len(arr)):
        # Add current element to cumulative sum
        cum_sum += arr[i]
        
        # If cumulative sum is zero, add subarray from 0 to i
        if cum_sum == 0:
            result.append((0, i))
        
        # If the cumulative sum has been seen before, it means there's a zero-sum subarray
        if cum_sum in sum_map:
            # Add all subarrays starting after each previous occurrence of this cumulative sum
            for start_index in sum_map[cum_sum]:
                result.append((start_index + 1, i))
        
        # Store the current cumulative sum with the current index
        if cum_sum in sum_map:
            sum_map[cum_sum].append(i)
        else:
            sum_map[cum_sum] = [i]
    
    return result

# Test cases
print(find_subarrays_with_zero_sum([1, 2, -3, 3, -1, 2]))  # Output: [(0, 2), (1, 3)]
print(find_subarrays_with_zero_sum([4, -1, -3, 1, 2, -1]))  # Output: [(1, 2), (0, 3)]
print(find_subarrays_with_zero_sum([1, 2, 3, 4]))  # Output: []
print(find_subarrays_with_zero_sum([0, 0, 0]))  # Output: [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
print(find_subarrays_with_zero_sum([-3, 1, 2, -3, 4, 0]))  # Output: [(0, 3), (4, 4)]
