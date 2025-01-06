class Solution:
    def sumClosest(self, arr, target):
        # Sort the array to apply the two-pointer technique
        arr.sort()
        n = len(arr)
        closest_pair = []
        closest_sum = float('inf')
        max_abs_diff = float('-inf')
        
        # Two-pointer approach
        left, right = 0, n - 1
        while left < right:
            current_sum = arr[left] + arr[right]
            diff = abs(current_sum - target)
            
            if diff < abs(closest_sum - target):
                # Update closest sum and pair
                closest_sum = current_sum
                closest_pair = [arr[left], arr[right]]
                max_abs_diff = abs(arr[right] - arr[left])
            elif diff == abs(closest_sum - target):
                # If the sum is equally close, choose the pair with max absolute difference
                current_abs_diff = abs(arr[right] - arr[left])
                if current_abs_diff > max_abs_diff:
                    closest_pair = [arr[left], arr[right]]
                    max_abs_diff = current_abs_diff
            
            # Adjust pointers
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                break  # Exact match found
        
        return closest_pair
