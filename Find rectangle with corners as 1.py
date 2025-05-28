class Solution:    
    def ValidCorner(self, mat): 
        n = len(mat)
        m = len(mat[0])
        seen = set()

        for i in range(n):
            for c1 in range(m):
                if mat[i][c1] == 1:
                    for c2 in range(c1 + 1, m):
                        if mat[i][c2] == 1:
                            # If this column pair has been seen in a previous row
                            if (c1, c2) in seen:
                                return True
                            seen.add((c1, c2))
        return False
