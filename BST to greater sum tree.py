class Solution:
    def __init__(self):
        self.sum_so_far = 0  # This keeps track of the accumulated sum of greater nodes
        
    def transformTree(self, root):
        # Helper function for reverse inorder traversal
        def reverse_inorder(node):
            if not node:
                return
            
            # Step 1: Traverse right subtree (greater values)
            reverse_inorder(node.right)
            
            # Step 2: Process current node
            old_val = node.data
            node.data = self.sum_so_far
            self.sum_so_far += old_val
            
            # Step 3: Traverse left subtree (smaller values)
            reverse_inorder(node.left)
        
        reverse_inorder(root)
        return root
