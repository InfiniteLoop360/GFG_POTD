class Solution():
    def maxMinHeight(self, arr, k, w):
        n = len(arr)
        
        def canAchieve(target):
            diff = [0] * (n + 1)
            used = 0
            curr_add = 0
            
            for i in range(n):
                curr_add += diff[i]
                height = arr[i] + curr_add
                
                if height < target:
                    need = target - height
                    used += need
                    if used > k:
                        return False
                    
                    curr_add += need
                    if i + w < n:
                        diff[i + w] -= need
            
            return True
        
        low, high = min(arr), min(arr) + k
        ans = low
        
        while low <= high:
            mid = (low + high) // 2
            if canAchieve(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
