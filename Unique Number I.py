class Solution:
    def findUnique(self, arr):
        """
        :param arr: List[int] where every number appears exactly twice except one
        :return: the single number that appears only once
        """
        unique = 0
        for num in arr:
            unique ^= num
        return unique
