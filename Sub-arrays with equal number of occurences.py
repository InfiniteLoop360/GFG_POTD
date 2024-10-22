class Solution:
    def sameOccurrence(self, arr, x, y):
        count_x = 0  # Track count of x
        count_y = 0  # Track count of y
        prefix_diff = {0: 1}  # Start with diff 0 (before any elements)
        result = 0
        
        for num in arr:
            if num == x:
                count_x += 1
            if num == y:
                count_y += 1
            
            # Calculate current difference between count(x) and count(y)
            diff = count_x - count_y
            
            # If this difference has been seen before, increment result
            if diff in prefix_diff:
                result += prefix_diff[diff]
            
            # Update the prefix difference count in the hashmap
            if diff in prefix_diff:
                prefix_diff[diff] += 1
            else:
                prefix_diff[diff] = 1
        
        return result
