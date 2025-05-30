class Solution:
    def findMaxFork(self, root, k):
        result = -1  # Default if no value <= k is found
        current = root

        while current:
            if current.data <= k:
                result = current.data  # Current node is a valid candidate
                current = current.right  # Try to find a larger valid value
            else:
                current = current.left  # Discard this and go left

        return result
