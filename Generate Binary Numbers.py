from collections import deque

class Solution:
    def generateBinary(self, n):
        """
        Generate binary representations (as strings) for numbers 1..n in order.
        Returns a list of strings of length n.
        """
        if n <= 0:
            return []

        res = []
        q = deque()
        q.append("1")

        # generate n binary numbers
        for _ in range(n):
            s = q.popleft()
            res.append(s)
            # enqueue next two binary numbers derived from s
            q.append(s + "0")
            q.append(s + "1")

        return res
