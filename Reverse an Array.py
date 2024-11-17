class Solution:
    def reverseArray(self, arr):
        # Two-pointer approach
        left, right = 0, len(arr) - 1
        
        while left < right:
            # Swap elements
            arr[left], arr[right] = arr[right], arr[left]
            # Move pointers
            left += 1
            right -= 1
        
        return arr
