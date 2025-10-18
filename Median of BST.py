class Solution:
    def findMedian(self, root):
        # Helper function for inorder traversal
        def inorder(node, arr):
            if not node:
                return
            inorder(node.left, arr)
            arr.append(node.data)
            inorder(node.right, arr)

        # Store inorder traversal (sorted order)
        values = []
        inorder(root, values)
        
        n = len(values)

        # Odd number of elements
        if n % 2 == 1:
            return values[n // 2]
        else:
            # Even number of elements
            return values[(n // 2) - 1]
