class Solution:
    def floodFill(self, image, sr, sc, newColor):
        originalColor = image[sr][sc]
        if originalColor == newColor:
            return image
        
        n, m = len(image), len(image[0])
        
        def dfs(r, c):
            # Base case: boundary check or color mismatch
            if r < 0 or c < 0 or r >= n or c >= m or image[r][c] != originalColor:
                return
            # Fill color
            image[r][c] = newColor
            
            # Explore 4 directions
            dfs(r+1, c)  # Down
            dfs(r-1, c)  # Up
            dfs(r, c+1)  # Right
            dfs(r, c-1)  # Left
        
        dfs(sr, sc)
        return image
