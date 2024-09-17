def find_subarrays_with_zero_sum(arr):
    sum_map = {}
    result = []
    
  
    cum_sum = 0
    
  
    for i in range(len(arr)):
        cum_sum += arr[i]
        
   
        if cum_sum == 0:
            result.append((0, i))
        
       
        if cum_sum in sum_map:
            for start_index in sum_map[cum_sum]:
                result.append((start_index + 1, i))
        
       
        if cum_sum in sum_map:
            sum_map[cum_sum].append(i)
        else:
            sum_map[cum_sum] = [i]
    
    return result


print(find_subarrays_with_zero_sum([1, 2, -3, 3, -1, 2]))  
print(find_subarrays_with_zero_sum([4, -1, -3, 1, 2, -1]))  
print(find_subarrays_with_zero_sum([1, 2, 3, 4])) 
print(find_subarrays_with_zero_sum([0, 0, 0]))   
print(find_subarrays_with_zero_sum([-3, 1, 2, -3, 4, 0]))  
