class Solution:
    def alternateSort(self, arr):
        # Sort the array
        arr.sort()
        
        # Initialize pointers and result list
        left, right = 0, len(arr) - 1
        result = []
        
        # Fill result list in alternative high-low order
        while left <= right:
            if right >= left:
                result.append(arr[right])
                right -= 1
            if left <= right:
                result.append(arr[left])
                left += 1
        
        return result

