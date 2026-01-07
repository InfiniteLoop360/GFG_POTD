class Solution:
    def countDistinct(self, arr, k):
        MAX = 100001
        freq = [0] * MAX
        distinct = 0
        result = []

        for i in range(k):
            if freq[arr[i]] == 0:
                distinct += 1
            freq[arr[i]] += 1
        
        result.append(distinct)

        for i in range(k, len(arr)):
            out = arr[i - k]
            freq[out] -= 1
            if freq[out] == 0:
                distinct -= 1

            inp = arr[i]
            if freq[inp] == 0:
                distinct += 1
            freq[inp] += 1

            result.append(distinct)

        return result
