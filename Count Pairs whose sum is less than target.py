class Solution:
    def countPairs(self, arr, target):
        # Sort the array
        arr.sort()
        i, j = 0, len(arr) - 1
        count = 0
        
        # Two-pointer approach
        while i < j:
            if arr[i] + arr[j] < target:
                # All pairs from i to j will have a sum < target
                count += j - i
                i += 1  # Move the left pointer
            else:
                j -= 1  # Move the right pointer
        
        return count
