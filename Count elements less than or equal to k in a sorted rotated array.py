from bisect import bisect_right

class Solution:
    def countLessEqual(self, arr, x):
        n = len(arr)
        
        # Step 1: Find pivot (index of minimum element)
        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid
        pivot = low
        
        # Step 2: Count in both sorted parts
        count = 0
        
        # Right sorted part [pivot ... n-1]
        count += bisect_right(arr[pivot:], x)
        
        # Left sorted part [0 ... pivot-1]
        count += bisect_right(arr[:pivot], x)
        
        return count
