# Case [Best, Average, Worst] = [O(n log n), O(n log n), O(n^2)]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    
    left = [ x for x in arr if x < pivot ]
    middle = [ x for x in arr if x == pivot ]
    right = [ x for x in arr if x > pivot ]
    
    return quick_sort(left) + middle + quick_sort(right)

arr = [7, 3, 9, 1, 5]

print(quick_sort(arr))