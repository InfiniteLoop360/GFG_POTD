class Solution:
    def kthSmallest(self, root, k):
        self.count = 0
        self.ans = -1
        
        def inorder(node):
            if not node or self.ans != -1:
                return
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.ans = node.data
                return
            inorder(node.right)
        
        inorder(root)
        return self.ans
