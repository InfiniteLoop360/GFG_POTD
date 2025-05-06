class Solution:
    def LeftView(self, root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.pop(0)

                # The first node at each level is part of the left view
                if i == 0:
                    result.append(node.data)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
