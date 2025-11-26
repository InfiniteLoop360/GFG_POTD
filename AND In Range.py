class Solution:
    def andInRange(self, l, r):
        shift = 0
        
        # Find common prefix
        while l < r:
            l >>= 1
            r >>= 1
            shift += 1
        
        return l << shift
