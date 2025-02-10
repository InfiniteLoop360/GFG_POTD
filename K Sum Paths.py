class Solution:
    def sumK(self, root, k):
        def helper(node, prefix_sum, curr_sum):
            if not node:
                return 0
            
            # Update the current sum
            curr_sum += node.data
            
            # Check if there exists a prefix sum that equals (curr_sum - k)
            count = prefix_sum.get(curr_sum - k, 0)
            
            # Update the prefix sum map
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
            
            # Recur for left and right subtrees
            count += helper(node.left, prefix_sum, curr_sum)
            count += helper(node.right, prefix_sum, curr_sum)
            
            # Backtrack: Remove current sum from prefix map
            prefix_sum[curr_sum] -= 1
            if prefix_sum[curr_sum] == 0:
                del prefix_sum[curr_sum]
            
            return count

        # HashMap to store prefix sums
        return helper(root, {0: 1}, 0)
