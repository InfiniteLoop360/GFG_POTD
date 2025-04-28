class Solution:
    # Function to return the maximum sum of non-adjacent nodes.
    def getMaxSum(self, root):
        def solve(node):
            if not node:
                return (0, 0)  # (include_node, exclude_node)

            left_include, left_exclude = solve(node.left)
            right_include, right_exclude = solve(node.right)

            # If we include current node, we can't include its children
            include_node = node.data + left_exclude + right_exclude

            # If we exclude current node, we can include or exclude its children (whichever is better)
            exclude_node = max(left_include, left_exclude) + max(right_include, right_exclude)

            return (include_node, exclude_node)
        
        include_root, exclude_root = solve(root)
        return max(include_root, exclude_root)
