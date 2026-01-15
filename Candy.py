class Solution:
    def minCandy(self, arr):
        n = len(arr)
        
        # Step 1: everyone gets at least 1 candy
        candies = [1] * n
        
        # Step 2: left to right
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Step 3: right to left
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)
