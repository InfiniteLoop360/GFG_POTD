class Solution:
    def findDuplicate(self, arr):
        """
        :param arr: List[int] of size n, containing all numbers from 1 to n-1
                    with exactly one number repeated
        :return: the repeated integer
        """
        n = len(arr)
        total = sum(arr)
        expected = (n - 1) * n // 2
        return total - expected
