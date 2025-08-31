class Solution:
    def maxWater(self, arr):
        n = len(arr)
        if n < 2:
            return 0  # a single line can't hold water
        
        left, right = 0, n - 1
        best = 0
        
        while left < right:
            # Current container is between left and right
            height = min(arr[left], arr[right])
            width = right - left
            best = max(best, height * width)
            
            # Move the pointer at the shorter line inward to seek a taller boundary
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        
        return best
