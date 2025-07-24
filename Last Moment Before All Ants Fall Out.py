class Solution:
    def getLastMoment(self, n, left, right):
        max_left_time = max(left) if left else 0
        max_right_time = max(n - r for r in right) if right else 0
        return max(max_left_time, max_right_time)
