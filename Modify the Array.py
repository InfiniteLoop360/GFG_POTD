class Solution:
    def modifyAndRearrangeArr(self, arr):
        n = len(arr)
        
        # Step 1: Modify the array by doubling the current element if next is equal and non-zero
        for i in range(n - 1):
            if arr[i] == arr[i + 1] and arr[i] != 0:
                arr[i] *= 2
                arr[i + 1] = 0
        
        # Step 2: Shift non-zero elements to the front and fill the rest with 0's
        non_zero_pos = 0
        
        # Place all non-zero elements in the beginning of the array
        for i in range(n):
            if arr[i] != 0:
                arr[non_zero_pos] = arr[i]
                non_zero_pos += 1
        
        # Fill the remaining positions with 0's
        while non_zero_pos < n:
            arr[non_zero_pos] = 0
            non_zero_pos += 1
        
        return arr
