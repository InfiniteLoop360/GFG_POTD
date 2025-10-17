class Solution:
    def __init__(self):
        self.sum_so_far = 0  
        
    def transformTree(self, root):
        def reverse_inorder(node):
            if not node:
                return
    
            reverse_inorder(node.right)

            old_val = node.data
            node.data = self.sum_so_far
            self.sum_so_far += old_val

            reverse_inorder(node.left)
        
        reverse_inorder(root)
        return root
