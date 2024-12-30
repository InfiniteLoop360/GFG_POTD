class Solution:
    # Function to return the count of number of elements in the union of two arrays.
    def findUnion(self, a, b):
        # Use a set to automatically handle duplicates
        union_set = set(a).union(set(b))
        
        # Return the size of the union set
        return len(union_set)
