class Solution:
    def getCount(self, n):
        if n == 1:
            return 10

        moves = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [2, 1, 3, 5],
            3: [3, 2, 6],
            4: [4, 1, 5, 7],
            5: [5, 2, 4, 6, 8],
            6: [6, 3, 5, 9],
            7: [7, 4, 8],
            8: [8, 5, 7, 9, 0],
            9: [9, 6, 8],
        }

        # Initialize dp array: dp[i][digit]
        dp = [[0] * 10 for _ in range(n + 1)]

        # Base case: length 1, all digits count as 1
        for digit in range(10):
            dp[1][digit] = 1

        # Fill dp table
        for i in range(2, n + 1):
            for digit in range(10):
                for nei in moves[digit]:
                    dp[i][digit] += dp[i - 1][nei]

        # Total combinations of length n
        return sum(dp[n])
