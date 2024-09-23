class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        repeating = missing = 0

        for i in range(n):
            index = abs(arr[i]) - 1
            if arr[index] < 0:
                repeating = abs(arr[i])
            else:
                arr[index] = -arr[index]

        for i in range(n):
            if arr[i] > 0:
                missing = i + 1
                break

        return repeating, missing
