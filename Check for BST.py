# Approach1: Recursive Range Check: Ensure each node's value lies within a valid range.

class Solution:
    
    # Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        def validate(node, min_val, max_val):
            if not node:
                return True
            if not (min_val < node.data < max_val):
                return False
            return validate(node.left, min_val, node.data) and validate(node.right, node.data, max_val)

        return validate(root, float('-inf'), float('inf'))



# Approach2: Inorder Traversal: Track the last visited node and verify it follows ascending order.

class Solution:
    
    # Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        prev = None

        def inorder(node):
            nonlocal prev
            if not node:
                return True
            if not inorder(node.left):
                return False
            if prev is not None and prev >= node.data:
                return False
            prev = node.data
            return inorder(node.right)

        return inorder(root)
