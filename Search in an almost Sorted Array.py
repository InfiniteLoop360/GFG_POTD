class Solution:
    def findTarget(self, arr, target):
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            # Check mid
            if arr[mid] == target:
                return mid
            # Check mid-1
            if mid - 1 >= low and arr[mid - 1] == target:
                return mid - 1
            # Check mid+1
            if mid + 1 <= high and arr[mid + 1] == target:
                return mid + 1

            # Decide to move left or right
            if arr[mid] > target:
                high = mid - 2  # Skip mid and mid-1
            else:
                low = mid + 2   # Skip mid and mid+1

        return -1
