def find_duplicate(arr):
    tortoise = arr[0]
    hare = arr[0]
    
    while True:
        tortoise = arr[tortoise] 
        hare = arr[arr[hare]]     
        if tortoise == hare:
            break  

   
    tortoise = arr[0]
    while tortoise != hare:
        tortoise = arr[tortoise]  
        hare = arr[hare]          

    return hare  

print(find_duplicate([1, 3, 4, 2, 2]))  
print(find_duplicate([3, 1, 3, 4, 2]))  
print(find_duplicate([1, 1]))           
print(find_duplicate([1, 4, 4, 2, 3]))  
