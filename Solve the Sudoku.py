class Solution:
    def solveSudoku(self, mat):
        self.solve(mat)

    def solve(self, board):
        empty_cell = self.find_empty(board)
        if not empty_cell:
            return True  # No empty space left, solution found

        row, col = empty_cell

        for num in range(1, 10):
            if self.isValid(board, row, col, num):
                board[row][col] = num  # Place the number

                if self.solve(board):
                    return True  # If next step is valid, continue solving

                board[row][col] = 0  # Backtrack if solution is not found

        return False  # No valid number found, trigger backtracking

    def find_empty(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)  # Return first empty position
        return None

    def isValid(self, board, row, col, num):
        # Check Row and Column
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        
        # Check 3x3 Sub-grid
        box_x, box_y = row // 3 * 3, col // 3 * 3
        for i in range(3):
            for j in range(3):
                if board[box_x + i][box_y + j] == num:
                    return False

        return True  # Number is valid
