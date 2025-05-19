class Solution:
    def findPreSuc(self, root, key):
        self.pre = None
        self.suc = None

        def inorder_search(node):
            if not node:
                return
            
            if node.data == key:
                # Find predecessor (max in left subtree)
                if node.left:
                    tmp = node.left
                    while tmp.right:
                        tmp = tmp.right
                    self.pre = tmp

                # Find successor (min in right subtree)
                if node.right:
                    tmp = node.right
                    while tmp.left:
                        tmp = tmp.left
                    self.suc = tmp

            elif key < node.data:
                self.suc = node
                inorder_search(node.left)
            else:
                self.pre = node
                inorder_search(node.right)

        inorder_search(root)
        return (self.pre, self.suc)
