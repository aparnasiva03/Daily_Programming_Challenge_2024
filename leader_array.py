def find_leaders(arr):
    n = len(arr)
    if n == 0:
        return []
    
    max_from_right = arr[-1]
    leaders = [max_from_right]
    
    for i in range(n-2, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]
    
    leaders.reverse()
    
    return leaders


arr = [16, 17, 4, 3, 5, 2]
print("Leaders:", find_leaders(arr))  


arr = [1, 2, 3, 4, 0]
print("Leaders:", find_leaders(arr)) 

arr = [7, 10, 4, 10, 6, 5, 2]
print("Leaders:", find_leaders(arr))  

arr = [5]
print("Leaders:", find_leaders(arr))  
arr = [100, 50, 20, 10]
print("Leaders:", find_leaders(arr))  


arr = list(range(1, 1000001))  
print("Leaders:", find_leaders(arr)) 
