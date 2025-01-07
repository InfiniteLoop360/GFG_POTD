
class Solution:
    def countPairs(self, arr, target):
        count = 0
        left, right = 0, len(arr) - 1
        
        while left < right:
            current_sum = arr[left] + arr[right]
            
            if current_sum == target:
                # Handle duplicates on both sides
                if arr[left] == arr[right]:
                    n = right - left + 1
                    count += n * (n - 1) // 2
                    break
                else:
                    # Count duplicates on the left
                    left_val, left_count = arr[left], 1
                    while left + 1 < right and arr[left + 1] == left_val:
                        left += 1
                        left_count += 1
                    
                    # Count duplicates on the right
                    right_val, right_count = arr[right], 1
                    while right - 1 > left and arr[right - 1] == right_val:
                        right -= 1
                        right_count += 1
                    
                    # Add the product of counts (left_count * right_count)
                    count += left_count * right_count
                
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return count
