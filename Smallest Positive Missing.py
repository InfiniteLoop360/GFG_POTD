class Solution:
    def missingNumber(self, arr):
        n = len(arr)
        
        # Step 1: Place each number in its correct position if possible
        i = 0
        while i < n:
            if 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
            else:
                i += 1

        # Step 2: Find the first index i such that arr[i] != i+1
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1

        # Step 3: If all positions are correct
        return n + 1
