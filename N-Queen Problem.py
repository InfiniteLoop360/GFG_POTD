class Solution:
    def nQueen(self, n):
        result = []
        board = []
        self.solve(0, n, set(), set(), set(), [], result)
        return result

    def solve(self, col, n, rows, main_diag, anti_diag, path, result):
        if col == n:  # Base Case: All queens are placed
            result.append(path[:])  # Store the solution
            return
        
        for row in range(1, n + 1):  # Try placing a queen in each row
            if row in rows or (row - col) in main_diag or (row + col) in anti_diag:
                continue  # Skip if under attack
            
            # Place the queen
            rows.add(row)
            main_diag.add(row - col)
            anti_diag.add(row + col)
            path.append(row)

            # Recur for next column
            self.solve(col + 1, n, rows, main_diag, anti_diag, path, result)

            # Backtrack
            rows.remove(row)
            main_diag.remove(row - col)
            anti_diag.remove(row + col)
            path.pop()
