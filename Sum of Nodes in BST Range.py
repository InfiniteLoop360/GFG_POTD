class Solution:
    def nodeSum(self, root, l, r):

        def dfs(node):
            if node is None:
                return 0

            # If node's value is less than l, skip left subtree
            if node.data < l:
                return dfs(node.right)

            # If node's value is greater than r, skip right subtree
            if node.data > r:
                return dfs(node.left)

            # node.data is in [l, r]: include it and search both sides
            return node.data + dfs(node.left) + dfs(node.right)

        return dfs(root)
