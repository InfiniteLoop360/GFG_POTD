class Solution:
    def findMaxSum(self, root): 
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Compute maximum downward path sums
            left = dfs(node.left)
            right = dfs(node.right)

            # Path through current node
            current_sum = node.data + max(0, left) + max(0, right)

            # Update global maximum
            self.max_sum = max(self.max_sum, current_sum)

            # Return max downward path sum to parent
            return node.data + max(0, max(left, right))

        dfs(root)
        return self.max_sum
