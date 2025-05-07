class Solution:
    def Paths(self, root):
        def dfs(node, path, res):
            if not node:
                return
            
            path.append(node.data)
            
            # If it's a leaf node, save the path
            if not node.left and not node.right:
                res.append(path[:])
            else:
                dfs(node.left, path, res)
                dfs(node.right, path, res)
            
            # Backtrack
            path.pop()
        
        result = []
        dfs(root, [], result)
        return result
