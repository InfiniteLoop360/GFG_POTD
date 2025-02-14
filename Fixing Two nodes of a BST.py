# Using Inorder Traversal to Find Swapped Nodes (O(n) time, O(h) space)

class Solution:
    def correctBST(self, root):
        first = middle = last = prev = None
        
        def inorder(node):
            nonlocal first, middle, last, prev
            if not node:
                return
            
            inorder(node.left)
            
            if prev and node.data < prev.data:
                if not first:
                    first, middle = prev, node
                else:
                    last = node
            
            prev = node
            inorder(node.right)
        
        inorder(root)
        
        if first and last:
            first.data, last.data = last.data, first.data
        elif first and middle:
            first.data, middle.data = middle.data, first.data
        
        return 1



# Morris Traversal for O(1) Space!

class Solution:
    def correctBST(self, root):
        first = middle = last = prev = None
        current = root
        
        while current:
            if not current.left:
                if prev and current.data < prev.data:
                    if not first:
                        first, middle = prev, current
                    else:
                        last = current
                prev = current
                current = current.right
            else:
                pre = current.left
                while pre.right and pre.right != current:
                    pre = pre.right
                if not pre.right:
                    pre.right = current
                    current = current.left
                else:
                    pre.right = None
                    if prev and current.data < prev.data:
                        if not first:
                            first, middle = prev, current
                        else:
                            last = current
                    prev = current
                    current = current.right
        
        if first and last:
            first.data, last.data = last.data, first.data
        elif first and middle:
            first.data, middle.data = middle.data, first.data
        
        return 1

