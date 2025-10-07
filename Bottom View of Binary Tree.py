from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def bottomView(self, root):
        if not root:
            return []
        q = deque()
        q.append((root, 0))
        hd_map = {}

        while q:
            node, hd = q.popleft()
            hd_map[hd] = node.data
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
        result = [hd_map[hd] for hd in sorted(hd_map)]
        return result
