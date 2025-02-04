class Solution:
    def diameter(self, root):
        def dfs(node):
            if not node:
                return 0, 0  # (height, diameter)
            
            left_height, left_diameter = dfs(node.left)
            right_height, right_diameter = dfs(node.right)
            
            # Diameter at current node = left height + right height
            curr_diameter = left_height + right_height
            
            # Max diameter so far
            max_diameter = max(curr_diameter, left_diameter, right_diameter)
            
            # Return updated height and diameter
            return max(left_height, right_height) + 1, max_diameter
        
        return dfs(root)[1]
