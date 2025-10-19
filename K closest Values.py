class Solution:
    def getKClosest(self, root, target, k):
        vals = []
        
        def inorder(node):
            if not node: return
            inorder(node.left)
            vals.append(node.data)
            inorder(node.right)
        
        inorder(root)
        vals.sort(key=lambda x: (abs(x - target), x))
        return vals[:k]
