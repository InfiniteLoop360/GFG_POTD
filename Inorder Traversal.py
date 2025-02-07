class Solution:
    def inOrder(self, root):
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, node, result):
        if node:
            self.traverse(node.left, result)  # Visit left subtree
            result.append(node.data)         # Visit node
            self.traverse(node.right, result) # Visit right subtree
