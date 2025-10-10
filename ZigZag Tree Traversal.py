from collections import deque


class Solution:
    def zigZagTraversal(self, root):
        if not root:
            return []

        res = []
        q = deque([root])
        left_to_right = True

        while q:
            level_size = len(q)
            level = []  # collect values for this level

            for _ in range(level_size):
                node = q.popleft()
                level.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # If this level should be right-to-left, reverse the collected values
            if not left_to_right:
                level.reverse()

            res.extend(level)
            left_to_right = not left_to_right

        return res
