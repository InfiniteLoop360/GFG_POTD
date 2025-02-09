class Solution:
    def findMaxSum(self, root):
        # Initialize the max sum variable
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            # Get max sum from left and right subtrees
            left_sum = max(0, dfs(node.left))  # Ignore negative paths
            right_sum = max(0, dfs(node.right))
            
            # Calculate max path sum passing through this node
            current_max = left_sum + right_sum + node.data
            
            # Update global max sum
            self.max_sum = max(self.max_sum, current_max)
            
            # Return the max single path sum to propagate up
            return max(left_sum, right_sum) + node.data

        dfs(root)  # Start DFS from root
        return self.max_sum
