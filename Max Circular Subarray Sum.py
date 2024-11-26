def circularSubarraySum(arr):
    n = len(arr)
    
    # Function to find the maximum subarray sum using Kadane's algorithm
    def kadane(arr):
        max_ending_here = max_so_far = arr[0]
        for x in arr[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
    
    # Step 1: Find the maximum subarray sum using Kadane's algorithm
    max_kadane = kadane(arr)
    
    # Step 2: Find the maximum circular subarray sum
    total_sum = sum(arr)
    # Invert the array elements
    for i in range(n):
        arr[i] = -arr[i]
    
    # Maximum circular subarray sum is total_sum + max subarray sum of the inverted array
    max_wrap = total_sum + kadane(arr)
    
    # Edge case: If all numbers are negative, max_wrap will be 0; hence return max_kadane
    if max_wrap == 0:
        return max_kadane
    
    return max(max_kadane, max_wrap)
