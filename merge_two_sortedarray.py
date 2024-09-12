import math


def next_gap(gap):
    if gap <= 1:
        return 0
    return math.ceil(gap / 2)

def merge(arr1, arr2, m, n):
    gap = m + n
    gap = next_gap(gap)
    
    while gap > 0:
        i = 0
        while i + gap < m:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]  
            i += 1
        
 
        j = max(0, gap - m)
        i = 0
        while i < m and j < n:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]  
            i += 1
            j += 1

       
        j = 0
        while j + gap < n:
            if arr2[j] > arr2[j + gap]:
                arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]  
            j += 1
        
        gap = next_gap(gap)


arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
m = len(arr1)
n = len(arr2)

merge(arr1, arr2, m, n)

print("arr1:", arr1)
print("arr2:", arr2)
