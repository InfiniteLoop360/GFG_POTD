class Solution:
    def countWays(self, s):
        n = len(s)
        vals = []
        ops = []
        for char in s:
            if char == 'T' or char == 'F':
                vals.append(char == 'T')
            else:
                ops.append(char)
        
        m = len(vals)
        dp_true = [[0] * m for _ in range(m)]
        dp_false = [[0] * m for _ in range(m)]
        
        for i in range(m):
            dp_true[i][i] = 1 if vals[i] else 0
            dp_false[i][i] = 1 if not vals[i] else 0
        
        for length in range(2, m + 1):
            for i in range(m - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    op = ops[k]
                    true_i_k = dp_true[i][k]
                    false_i_k = dp_false[i][k]
                    true_k1_j = dp_true[k + 1][j]
                    false_k1_j = dp_false[k + 1][j]
                    
                    if op == '&':
                        dp_true[i][j] += true_i_k * true_k1_j
                        dp_false[i][j] += (true_i_k * false_k1_j + false_i_k * true_k1_j + false_i_k * false_k1_j)
                    elif op == '|':
                        dp_true[i][j] += (true_i_k * true_k1_j + true_i_k * false_k1_j + false_i_k * true_k1_j)
                        dp_false[i][j] += false_i_k * false_k1_j
                    elif op == '^':
                        dp_true[i][j] += (true_i_k * false_k1_j + false_i_k * true_k1_j)
                        dp_false[i][j] += (true_i_k * true_k1_j + false_i_k * false_k1_j)
        
        return dp_true[0][m - 1]
