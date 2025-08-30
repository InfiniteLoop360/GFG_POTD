class Solution:
    def celebrity(self, mat):
        n = len(mat)
        if n == 0:
            return -1
        # two-pointer elimination to get one candidate
        i, j = 0, n - 1
        while i < j:
            if mat[i][j] == 1:
                # i knows j -> i cannot be celebrity
                i += 1
            else:
                # i does NOT know j -> j cannot be celebrity
                j -= 1
        candidate = i

        # verify candidate: candidate should not know anyone else
        for col in range(n):
            if col == candidate:
                continue
            if mat[candidate][col] != 0:
                return -1

        # verify everyone else knows candidate
        for row in range(n):
            if row == candidate:
                continue
            if mat[row][candidate] != 1:
                return -1

        return candidate

        
