class Solution:
    def maxProduct(self, arr):
        # Initialize variables to store the maximum and minimum product up to the current index
        max_product = arr[0]
        min_product = arr[0]
        result = arr[0]
        
        # Traverse the array starting from the second element
        for i in range(1, len(arr)):
            # If the current element is negative, swap max_product and min_product
            if arr[i] < 0:
                max_product, min_product = min_product, max_product
            
            # Update max_product and min_product
            max_product = max(arr[i], arr[i] * max_product)
            min_product = min(arr[i], arr[i] * min_product)
            
            # Update the result with the maximum product found so far
            result = max(result, max_product)
        
        return result
