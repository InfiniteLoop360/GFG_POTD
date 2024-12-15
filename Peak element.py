class Solution:
    def peakElement(self, arr):
        # Start binary search
        low, high = 0, len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Check if mid is a peak
            if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]):
                return mid
            
            # If left neighbor is greater, move to the left half
            elif mid > 0 and arr[mid - 1] > arr[mid]:
                high = mid - 1
            
            # Otherwise, move to the right half
            else:
                low = mid + 1
