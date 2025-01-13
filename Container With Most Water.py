class Solution:
    def maxWater(self, arr):
        left = 0
        right = len(arr) - 1
        max_area = 0
        
        while left < right:
            # Calculate the area formed by the two lines
            height = min(arr[left], arr[right])
            width = right - left
            current_area = height * width
            
            # Update max_area if the current area is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
