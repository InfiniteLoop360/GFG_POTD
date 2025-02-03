class Solution:
    # Function to find the height of a binary tree.
    def height(self, root):
        if not root:
            return -1  # Since height is counted as edges, return -1 for an empty tree.
        return 1 + max(self.height(root.left), self.height(root.right))
