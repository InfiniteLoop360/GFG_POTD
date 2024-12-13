class Solution:
    def findMin(self, arr):
        # Binary search to find the minimum element
        low, high = 0, len(arr) - 1

        while low < high:
            mid = (low + high) // 2
            # If middle element is greater than the last element, the min is to the right
            if arr[mid] > arr[high]:
                low = mid + 1
            else:  # The min is at mid or to the left
                high = mid
        
        return arr[low]
