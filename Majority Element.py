class Solution:
    def majorityElement(self, arr):
        """
        :param arr: List[int] of length >= 1
        :return: the element appearing more than len(arr)//2 times, or -1 if none exists
        """
        # Phase 1: Find a candidate using Boyer–Moore Voting
        candidate = None
        count = 0
        for num in arr:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        # Phase 2: Verify the candidate
        if arr.count(candidate) > len(arr) // 2:
            return candidate
        return -1
