class Solution:
    def sortArray(self, arr, A, B, C):
        def f(x):
            return A * x * x + B * x + C
        
        n = len(arr)
        res = [0] * n
        i, j = 0, n - 1
        index = n - 1 if A >= 0 else 0
        
        while i <= j:
            left = f(arr[i])
            right = f(arr[j])
            if A >= 0:
                if left > right:
                    res[index] = left
                    i += 1
                else:
                    res[index] = right
                    j -= 1
                index -= 1
            else:
                if left < right:
                    res[index] = left
                    i += 1
                else:
                    res[index] = right
                    j -= 1
                index += 1
                
        return res
