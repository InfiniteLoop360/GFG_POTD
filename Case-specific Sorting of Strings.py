class Solution:
    def caseSort(self, s):
        upper = sorted([ch for ch in s if ch.isupper()])
        lower = sorted([ch for ch in s if ch.islower()])

        res = []
        i = j = 0

        for ch in s:
            if ch.isupper():
                res.append(upper[i])
                i += 1
            else:
                res.append(lower[j])
                j += 1

        return ''.join(res)
