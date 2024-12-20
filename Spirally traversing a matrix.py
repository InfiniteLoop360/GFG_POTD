class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # Initialize boundaries
        top, bottom = 0, len(mat) - 1
        left, right = 0, len(mat[0]) - 1

        result = []

        # Loop until all elements are traversed
        while top <= bottom and left <= right:
            # Traverse from left to right
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1

            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1

            if top <= bottom:
                # Traverse from right to left
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1

            if left <= right:
                # Traverse from bottom to top
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1

        return result
