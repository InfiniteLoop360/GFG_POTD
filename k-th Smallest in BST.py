# Inorder Traversal (Primary Approach)

class Solution:
    def kthSmallest(self, root, k):
        count = 0
        result = -1
        
        def inorder(node):
            nonlocal count, result
            if not node or result != -1:
                return
            inorder(node.left)
            count += 1
            if count == k:
                result = node.data
                return
            inorder(node.right)

        inorder(root)
        return result


# Bonus Code (Iterative Approach)

class Solution:
    def kthSmallest(self, root, k):
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.data
            root = root.right

