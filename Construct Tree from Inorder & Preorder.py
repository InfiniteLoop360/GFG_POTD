class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, preorder):
        inorder_map = {value: idx for idx, value in enumerate(inorder)}
        self.pre_index = 0
        
        def construct_tree(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.pre_index]
            self.pre_index += 1
            root = Node(root_val)
            
            root.left = construct_tree(left, inorder_map[root_val] - 1)
            root.right = construct_tree(inorder_map[root_val] + 1, right)
            
            return root

        return construct_tree(0, len(inorder) - 1)

    # Function to print postorder traversal
    def postorderTraversal(self, root):
        result = []
        
        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                result.append(node.data)
        
        postorder(root)
        return result
