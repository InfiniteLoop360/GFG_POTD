class Solution:
    def countBSTs(self, arr):
        def catalan_numbers(n):
            C = [0] * (n + 1)
            C[0] = 1
            for i in range(1, n + 1):
                for j in range(i):
                    C[i] += C[j] * C[i - 1 - j]
            return C
        
        n = len(arr)
        C = catalan_numbers(n)
        sorted_arr = sorted(arr)
        res = []
        
        for x in arr:
            L = sum(1 for val in sorted_arr if val < x)
            R = sum(1 for val in sorted_arr if val > x)
            res.append(C[L] * C[R])
        
        return res
