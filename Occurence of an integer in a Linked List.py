class Solution:
    def count(self, head, key):
        # Initialize the counter
        count = 0
        # Start traversing from the head node
        current = head
        while current:
            # Check if the current node's data is equal to the key
            if current.data == key:
                count += 1
            # Move to the next node
            current = current.next
        return count
