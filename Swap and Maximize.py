class Solution:
    def maxSum(self, arr):
        # Sort the array
        arr.sort()
        
        # Rearrange the array to maximize sum of absolute differences
        n = len(arr)
        rearranged = []
        i, j = 0, n - 1
        
        # Alternate placing smallest and largest remaining elements
        while i <= j:
            if i == j:
                rearranged.append(arr[i])
            else:
                rearranged.append(arr[i])
                rearranged.append(arr[j])
            i += 1
            j -= 1
        
        # Calculate the sum of absolute differences in a circular way
        max_sum = 0
        for k in range(n):
            max_sum += abs(rearranged[k] - rearranged[(k + 1) % n])
        
        return max_sum
