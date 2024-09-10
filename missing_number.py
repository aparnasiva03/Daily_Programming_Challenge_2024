def find_missing(arr):
    n = len(arr) + 1  
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum
    return missing_number

print(find_missing([1, 2, 4, 5]))  
print(find_missing([2, 3, 4, 5]))  
print(find_missing([1, 2, 3, 4]))  
print(find_missing([1]))           
print(find_missing(list(range(1, 1000000))))  
