class Solution:
    def countFreq(self, arr, target):
        # Binary search to find the first occurrence of the target
        def first_occurrence(arr, target):
            low, high = 0, len(arr) - 1
            first = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    first = mid
                    high = mid - 1  # Search in the left half
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return first

        # Binary search to find the last occurrence of the target
        def last_occurrence(arr, target):
            low, high = 0, len(arr) - 1
            last = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    last = mid
                    low = mid + 1  # Search in the right half
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return last

        first = first_occurrence(arr, target)
        if first == -1:
            return 0  # Target not found

        last = last_occurrence(arr, target)
        return last - first + 1
