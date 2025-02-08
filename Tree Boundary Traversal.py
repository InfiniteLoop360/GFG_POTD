class Solution:
    def boundaryTraversal(self, root):
        if not root:
            return []

        boundary = []

        # Helper function to add left boundary (excluding leaf nodes)
        def leftBoundary(node):
            while node:
                if node.left or node.right:
                    boundary.append(node.data)
                node = node.left if node.left else node.right

        # Helper function to add leaf nodes
        def addLeaves(node):
            if node:
                addLeaves(node.left)
                if not node.left and not node.right:
                    boundary.append(node.data)
                addLeaves(node.right)

        # Helper function to add right boundary (excluding leaf nodes, reversed later)
        def rightBoundary(node):
            temp = []
            while node:
                if node.left or node.right:
                    temp.append(node.data)
                node = node.right if node.right else node.left
            boundary.extend(reversed(temp))

        # 1. Add root if it's not a leaf
        if root.left or root.right:
            boundary.append(root.data)

        # 2. Add left boundary
        leftBoundary(root.left)

        # 3. Add leaf nodes
        addLeaves(root)

        # 4. Add right boundary in reverse
        rightBoundary(root.right)

        return boundary
