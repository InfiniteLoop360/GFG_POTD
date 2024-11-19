class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        # Step 1: Find the first decreasing element from the right
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1

        if i >= 0:  # There is a valid decreasing element
            # Step 2: Find the next larger element to arr[i] from the right
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
            # Step 3: Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

        # Step 4: Reverse the elements after index i
        arr[i + 1:] = reversed(arr[i + 1:])

        return arr
