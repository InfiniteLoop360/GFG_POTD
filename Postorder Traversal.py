class Solution:
    def postOrder(self, root):
        result = []

        def traverse(node):
            if not node:
                return
            traverse(node.left)
            traverse(node.right)
            result.append(node.data)

        traverse(root)
        return result
