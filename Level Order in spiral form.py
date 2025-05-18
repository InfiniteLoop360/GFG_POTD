from collections import deque

class Solution:
    def findSpiral(self, root):
        if not root:
            return []
        
        result = []
        q = deque()
        q.append(root)
        left_to_right = False  # Start with right to left (even level)
        
        while q:
            level_size = len(q)
            level_nodes = deque()
            
            for _ in range(level_size):
                node = q.popleft()
                if left_to_right:
                    level_nodes.append(node.data)
                else:
                    level_nodes.appendleft(node.data)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result.extend(level_nodes)
            left_to_right = not left_to_right  # Toggle the direction
        
        return result
