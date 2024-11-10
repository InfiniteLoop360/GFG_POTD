class Solution:
    # Function to return a list containing the union of the two arrays.
    def findUnion(self, a, b):
        result = []
        i, j = 0, 0
        
        # Traverse both arrays using two pointers
        while i < len(a) and j < len(b):
            # Avoid duplicates in the result
            if i > 0 and a[i] == a[i - 1]:
                i += 1
                continue
            if j > 0 and b[j] == b[j - 1]:
                j += 1
                continue
            
            # If both elements are the same, add one and move both pointers
            if a[i] == b[j]:
                result.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:  # Add the smaller element and move the pointer
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1
        
        # Add remaining elements from array a, avoiding duplicates
        while i < len(a):
            if i == 0 or a[i] != a[i - 1]:
                result.append(a[i])
            i += 1
        
        # Add remaining elements from array b, avoiding duplicates
        while j < len(b):
            if j == 0 or b[j] != b[j - 1]:
                result.append(b[j])
            j += 1
        
        return result

