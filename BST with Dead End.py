class Solution:
    def isDeadEnd(self, root):
        def dfs(node, min_val, max_val):
            if not node:
                return False

            if min_val == max_val:
                return True

            left = dfs(node.left, min_val, node.data - 1)
            right = dfs(node.right, node.data + 1, max_val)
            return left or right

        return dfs(root, 1, float('inf'))
