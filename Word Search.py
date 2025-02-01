class Solution:
    def isWordExist(self, mat, word):
        n, m = len(mat), len(mat[0])
        
        def dfs(i, j, index):
            if index == len(word):
                return True
            if i < 0 or i >= n or j < 0 or j >= m or mat[i][j] != word[index]:
                return False

            # Mark the cell as visited
            temp = mat[i][j]
            mat[i][j] = '#'  # Placeholder to mark as visited
            
            # Explore all four directions
            found = (dfs(i+1, j, index+1) or  # Down
                     dfs(i-1, j, index+1) or  # Up
                     dfs(i, j+1, index+1) or  # Right
                     dfs(i, j-1, index+1))    # Left
            
            # Restore the cell back after exploration
            mat[i][j] = temp
            
            return found
        
        # Start DFS from every cell that matches the first letter of word
        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False
