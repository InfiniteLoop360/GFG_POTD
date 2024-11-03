class Solution:
    # Function should return true if length is even, otherwise false
    def isLengthEven(self, head):
        # Initialize the counter
        count = 0
        
        # Traverse the linked list
        current = head
        while current:
            count += 1
            current = current.next
        
        # Return True if count is even, else return False
        return count % 2 == 0
