class Solution:
    def intersectionWithDuplicates(self, a, b):
        # Use sets to find unique elements in both arrays
        set_a = set(a)
        set_b = set(b)
        
        # Find the intersection of both sets
        result = list(set_a.intersection(set_b))
        
        return result
