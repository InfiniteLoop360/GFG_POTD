class Solution:
    def findPages(self, arr, k):
        n = len(arr)
        
        # If students > books, not possible
        if k > n:
            return -1
        
        low = max(arr)     # at least one student must take the largest book
        high = sum(arr)    # one student could take all
        
        result = high  # store best answer
        
        def isPossible(limit):
            students = 1
            pages = 0
            for p in arr:
                if pages + p > limit:
                    students += 1
                    pages = p
                    if students > k:  # too many students needed
                        return False
                else:
                    pages += p
            return True
        
        while low <= high:
            mid = (low + high) // 2
            if isPossible(mid):
                result = mid
                high = mid - 1  # try smaller maximum
            else:
                low = mid + 1   # need larger limit
        
        return result
