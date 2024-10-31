class Solution:
    # Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        # Create the new node
        new_node = Node(x)
        
        # Case 1: If the list is empty, return the new node as head
        if not head:
            return new_node
        
        # Case 2: If x is smaller than the head node's value, insert at the beginning
        if x <= head.data:
            new_node.next = head
            head.prev = new_node
            return new_node
        
        # Case 3: Traverse to find the correct position for insertion
        current = head
        while current.next and current.next.data < x:
            current = current.next
        
        # Insert the new node after the current node
        new_node.next = current.next
        new_node.prev = current
        
        # Update the next node's previous pointer if it exists
        if current.next:
            current.next.prev = new_node
            
        # Link the current node to the new node
        current.next = new_node
        
        return head
