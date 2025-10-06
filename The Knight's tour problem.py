class Solution:
    def knightTour(self, n):
        # Initialize chessboard
        board = [[-1 for _ in range(n)] for _ in range(n)]
        
        # Possible moves of a knight
        moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
        
        # Start from top-left corner
        board[0][0] = 0
        
        # Recursive function to solve the tour
        def solve(x, y, move_count):
            if move_count == n * n:
                return True
            
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
                    board[nx][ny] = move_count
                    if solve(nx, ny, move_count + 1):
                        return True
                    # Backtrack
                    board[nx][ny] = -1
            return False
        
        if solve(0, 0, 1):
            return board
        else:
            return []
