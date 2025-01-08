class Solution:
    # Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # Sort the array first
        arr.sort()
        n = len(arr)
        count = 0

        # Iterate over the array for the largest side
        for k in range(n - 1, 1, -1):
            i = 0
            j = k - 1
            while i < j:
                # If the sum of two smaller sides is greater than the largest side
                if arr[i] + arr[j] > arr[k]:
                    # All pairs between i and j are valid
                    count += (j - i)
                    j -= 1
                else:
                    i += 1

        return count
