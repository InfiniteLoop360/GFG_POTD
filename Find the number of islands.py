'''
Find the number of islands
Difficulty: MediumAccuracy: 42.12%Submissions: 198K+Points: 4
Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of '0's (Water) and '1's(Land). Find the number of islands.

Note: An island is either surrounded by water or the boundary of a grid and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

Examples:

Input: grid = [[0,1],[1,0],[1,1],[1,0]]
Output: 1
Explanation:
The grid is-
0 1
1 0
1 1
1 0
All lands are connected.
Input: grid = [[0,1,1,1,0,0,0],[0,0,1,1,0,1,0]]
Output: 2
Expanation:
The grid is-
0 1 1 1 0 0 0
0 0 1 1 0 2 0 
There are two islands in the grid. One island is marked by '1' and the other by '2'.
Expected Time Complexity: O(n*m)
Expected Space Complexity: O(n*m)

Constraints:
1 ≤ n, m ≤ 500
0 ≤ grid[i][j] ≤ 1Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of '0's (Water) and '1's(Land). Find the number of islands.


Note: An island is either surrounded by water or the boundary of a grid and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

Examples:

Input: grid = [[0,1],[1,0],[1,1],[1,0]]
Output: 1
Explanation:
The grid is-
0 1
1 0
1 1
1 0
All lands are connected.
Input: grid = [[0,1,1,1,0,0,0],[0,0,1,1,0,1,0]]
Output: 2
Expanation:
The grid is-
0 1 1 1 0 0 0
0 0 1 1 0 2 0 
There are two islands in the grid. One island is marked by '1' and the other by '2'.
Expected Time Complexity: O(n*m)
Expected Space Complexity: O(n*m)

Constraints:
1 ≤ n, m ≤ 500
grid[i][j] = {'0', '1'}
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### Problem Understanding:
The task is to find the number of islands in a grid where:
- A '1' represents land.
- A '0' represents water.
- Islands are connected groups of '1's, either horizontally, vertically, or diagonally.

### Approach:
1. **Grid Traversal:**
   We need to traverse the entire grid to explore every cell and check if it's part of an island (i.e., if it's '1').
   
2. **Marking Visited Cells:**
   Each time we encounter a '1', it marks the start of an island. We then use DFS to explore all its connected cells and mark them as visited to avoid recounting them as part of a different island.

3. **Iterative DFS:**
   Instead of using recursion (which could lead to stack overflow for large grids), we use an explicit stack (LIFO) to implement DFS. This stack will store the positions (i, j) of cells that we need to explore for connectivity.

4. **Direction Vectors:**
   To explore all 8 possible directions (horizontal, vertical, and diagonal), we define direction vectors that represent the movement from one cell to its neighboring cells.

5. **Counting Islands:**
   We increment the island count each time we initiate a DFS from an unvisited '1'. After completing the DFS for that island, all its connected land cells will be marked as visited.

### Detailed Steps:
1. **Initialization:**
   - Define direction vectors to move in 8 directions.
   - Initialize a variable `island_count` to store the number of islands.

2. **Grid Traversal:**
   - Iterate through each cell of the grid.
   - If the current cell contains a '1' (land) and hasn't been visited, it signifies a new island.
   
3. **DFS (Depth-First Search) Using Stack:**
   - Initialize a stack with the current cell’s coordinates.
   - Keep popping from the stack and exploring the neighboring cells using the direction vectors.
   - For each valid neighbor (within bounds and containing '1'), mark it visited and push it onto the stack.

4. **Increment Island Count:**
   - After finishing DFS for a cell, increment the `island_count` because you have completely explored one island.

5. **Continue Until All Cells are Explored:**
   - Repeat the above steps for every cell in the grid.

6. **Edge Cases:**
   - If the grid is empty or all cells are water ('0'), return 0.

'''
class Solution:
    def numIslands(self, grid):
        if not grid:  # Edge case: Empty grid
            return 0

        n, m = len(grid), len(grid[0])  # Get the number of rows (n) and columns (m)

        # Direction vectors for moving in 8 directions (up, down, left, right, and diagonals)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        def dfs_iterative(i, j):
            stack = [(i, j)]
            grid[i][j] = '0'  # Mark the cell as visited by changing '1' to '0'

            while stack:
                x, y = stack.pop()
                
                # Explore all 8 directions
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == '1':
                        stack.append((new_x, new_y))
                        grid[new_x][new_y] = '0'  # Mark this cell as visited

        island_count = 0  # Initialize island count

        for i in range(n):  # Traverse through the grid
            for j in range(m):
                if grid[i][j] == '1':  # If we find an unvisited land cell
                    island_count += 1  # This starts a new island
                    dfs_iterative(i, j)  # Run DFS to mark the entire island

        return island_count
'''
### Time Complexity:
- **O(n*m)** where `n` is the number of rows and `m` is the number of columns. This is because each cell is visited once when traversing the grid and performing DFS.

### Space Complexity:
- **O(n*m)** in the worst case, where the stack might hold all cells of the grid (in case the entire grid is filled with land).

### Example Walkthrough:
For the input grid:
```
0 1
1 0
1 1
1 0
```
The algorithm would:
1. Start from grid[0][1] (land), perform DFS, and mark the connected cells as visited.
2. Continue traversing the grid, but all other '1's are part of the same island already visited.
3. The final result will be `1` island.

### Why Iterative DFS?
Using recursion can lead to stack overflow if the grid is very large, especially if it contains a large connected island. By using an iterative approach with an explicit stack, we avoid this issue.
'''
