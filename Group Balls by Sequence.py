from collections import Counter

class Solution:
    def validgroup(self, arr, k):
        if len(arr) % k != 0:
            return False
        
        count = Counter(arr)
        sorted_keys = sorted(count)

        for num in sorted_keys:
            freq = count[num]
            if freq > 0:
                for i in range(num, num + k):
                    if count[i] < freq:
                        return False
                    count[i] -= freq
        return True
