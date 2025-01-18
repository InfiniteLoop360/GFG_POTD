# Node Class
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        
        while current is not None:
            next_node = current.next  # Store the next node
            current.next = prev       # Reverse the link
            prev = current            # Move `prev` one step forward
            current = next_node       # Move `current` one step forward
        
        return prev  # New head of the reversed list
