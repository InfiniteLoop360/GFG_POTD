from bisect import bisect_left

class Solution:
    def lis(self, arr):
        if not arr:
            return 0
        
        # List to store the smallest ending elements of increasing subsequences
        lis = []
        
        for num in arr:
            # Find the index where 'num' should be placed
            idx = bisect_left(lis, num)
            
            if idx == len(lis):
                lis.append(num)  # Extend the LIS
            else:
                lis[idx] = num  # Replace to maintain smallest possible ending element
        
        return len(lis)
