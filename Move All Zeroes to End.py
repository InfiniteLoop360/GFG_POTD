class Solution:
    def pushZerosToEnd(self, arr):
        # Initialize a pointer for the position to place non-zero elements
        non_zero_index = 0

        # Traverse the array
        for i in range(len(arr)):
            if arr[i] != 0:
                # Swap the current non-zero element with the element at non_zero_index
                arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
                non_zero_index += 1

        return arr
