class Solution:
    def getMaxSum(self, root):
        def solve(node):
            # Base case
            if not node:
                return (0, 0)  # (include, exclude)

            # Recur for left and right subtrees
            left = solve(node.left)
            right = solve(node.right)

            # If we include this node, we cannot include its children
            include = node.data + left[1] + right[1]

            # If we exclude this node, we can take max(include/exclude) from both children
            exclude = max(left) + max(right)

            return (include, exclude)

        # Compute result for root
        inc, exc = solve(root)
        return max(inc, exc)
