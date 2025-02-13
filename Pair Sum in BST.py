#Inorder Traversal & HashSet

class Solution:
    def findTarget(self, root, target):
        visited = set()
        
        def inorder(node):
            if not node:
                return False
            if inorder(node.left):  # Search in left subtree
                return True
            if (target - node.data) in visited:
                return True  # Pair found
            visited.add(node.data)  # Add current node to the set
            return inorder(node.right)  # Search in right subtree
        
        return inorder(root)


#Two-Pointer Method

class Solution:
    def findTarget(self, root, target):
        values = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.data)
            inorder(node.right)
        
        inorder(root)
        left, right = 0, len(values) - 1
        
        while left < right:
            total = values[left] + values[right]
            if total == target:
                return True
            elif total < target:
                left += 1
            else:
                right -= 1
                
        return False
