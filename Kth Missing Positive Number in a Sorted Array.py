class Solution:
    def kthMissing(self, arr, k):
        # Initialize variables
        missing_count = 0
        current = 1  # Start with the smallest positive number
        index = 0    # Pointer for the array

        # Iterate to find the k-th missing positive number
        while True:
            # Check if 'current' is missing in the array
            if index < len(arr) and arr[index] == current:
                # Move to the next element in the array
                index += 1
            else:
                # Count this number as missing
                missing_count += 1
                if missing_count == k:
                    return current
            # Move to the next positive number
            current += 1
