class Solution:
    # Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        if root is None:
            return
        
        # Swap the left and right child
        root.left, root.right = root.right, root.left
        
        # Recursively call for left and right subtrees
        self.mirror(root.left)
        self.mirror(root.right)
