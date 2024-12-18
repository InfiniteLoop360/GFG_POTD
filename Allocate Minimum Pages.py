class Solution:
    # Function to check if it is possible to allocate books with max pages as 'max_pages'.
    def isPossible(self, arr, k, max_pages):
        students = 1
        current_sum = 0
        
        for pages in arr:
            if pages > max_pages:
                return False
            if current_sum + pages > max_pages:
                students += 1
                current_sum = pages
                if students > k:
                    return False
            else:
                current_sum += pages
                
        return True

    # Function to find minimum number of pages.
    def findPages(self, arr, k):
        if len(arr) < k:
            return -1

        low, high = max(arr), sum(arr)
        result = high

        while low <= high:
            mid = (low + high) // 2
            if self.isPossible(arr, k, mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return result
