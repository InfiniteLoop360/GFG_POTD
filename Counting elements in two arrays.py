from bisect import bisect_right

class Solution:
    def countLessEq(self, a, b):
        b.sort()
        res = []
        for val in a:
            count = bisect_right(b, val)
            res.append(count)
        return res
