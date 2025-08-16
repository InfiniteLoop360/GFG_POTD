from functools import cmp_to_key

class Solution:
    def findLargest(self, arr):
        # Step 1: Convert numbers to strings
        arr = list(map(str, arr))
        
        # Step 2: Custom comparator
        def compare(x, y):
            if x + y > y + x:
                return -1   # x should come before y
            elif x + y < y + x:
                return 1    # y should come before x
            else:
                return 0
        
        # Step 3: Sort using comparator
        arr.sort(key=cmp_to_key(compare))
        
        # Step 4: Join result
        result = ''.join(arr)
        
        # Step 5: Handle leading zeros
        return '0' if result[0] == '0' else result
