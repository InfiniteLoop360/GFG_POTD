class Solution:
    def flatten(self, root):
        # Base case
        if root is None or root.next is None:
            return root
        
        # Recur for list on right
        root.next = self.flatten(root.next)
        
        # Merge current list with right list
        root = self.merge(root, root.next)
        
        return root
    
    def merge(self, a, b):
        # Dummy node to build result
        temp = Node(0)
        res = temp
        
        while a and b:
            if a.data < b.data:
                temp.bottom = a
                a = a.bottom
            else:
                temp.bottom = b
                b = b.bottom
            
            temp = temp.bottom
            temp.next = None  # Important: break next pointer
        
        # Attach remaining nodes
        if a:
            temp.bottom = a
        else:
            temp.bottom = b
        
        return res.bottom
