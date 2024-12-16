class Solution:
    def kthElement(self, a, b, k):
        # Two-pointer approach
        i, j, count = 0, 0, 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                count += 1
                if count == k:
                    return a[i]
                i += 1
            else:
                count += 1
                if count == k:
                    return b[j]
                j += 1
        
        # If we run out of elements in one array
        while i < len(a):
            count += 1
            if count == k:
                return a[i]
            i += 1

        while j < len(b):
            count += 1
            if count == k:
                return b[j]
            j += 1
