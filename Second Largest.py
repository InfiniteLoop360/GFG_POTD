class Solution:
    def getSecondLargest(self, arr):
        # Initialize the largest and second largest variables
        largest = second_largest = float('-inf')
        
        # Traverse the array
        for num in arr:
            if num > largest:  # Update largest and second largest
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num
        
        # If second largest remains unchanged, return -1
        return second_largest if second_largest != float('-inf') else -1
