from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])  # Initialize queue with the root node
        
        while queue:
            level_size = len(queue)
            level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.data)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(level)
        
        return result
