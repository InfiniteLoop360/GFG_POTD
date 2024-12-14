class Solution:
    def search(self, arr, key):
        # Initialize pointers
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            # Check if the mid element is the target
            if arr[mid] == key:
                return mid

            # Determine which side is sorted
            if arr[low] <= arr[mid]:
                # Left half is sorted
                if arr[low] <= key < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # Right half is sorted
                if arr[mid] < key <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1  # Key not found
