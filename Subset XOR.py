class Solution:
    def subsetXOR(self, n: int):
        # compute XOR of 1..n
        xor_all = 0
        for i in range(1, n + 1):
            xor_all ^= i
        
        # if already equal -> full lexicographically smallest largest subset
        if xor_all == n:
            return list(range(1, n + 1))
        
        # else one number must be removed
        missing = xor_all ^ n
        
        ans = []
        for i in range(1, n + 1):
            if i != missing:
                ans.append(i)
        
        return ans
