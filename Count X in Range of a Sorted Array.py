class Solution:
    def countXInRange(self, arr, queries):
        from bisect import bisect_left, bisect_right
        
        result = []
        
        for l, r, x in queries:
            # First occurrence of x
            left = bisect_left(arr, x)
            
            # First index greater than x
            right = bisect_right(arr, x) - 1
            
            # Adjust to query range
            start = max(left, l)
            end = min(right, r)
            
            if start <= end:
                result.append(end - start + 1)
            else:
                result.append(0)
        
        return result
