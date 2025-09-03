class Solution:
    def reverse(self, head):   # <-- changed from reverseDLL to reverse
        # Edge case: empty or single node list
        if head is None or head.next is None:
            return head
        
        curr = head
        new_head = None
        
        # Traverse and swap
        while curr:
            # Swap next and prev pointers
            curr.prev, curr.next = curr.next, curr.prev
            
            # Update new_head to the last processed node
            new_head = curr
            
            # Move to the "previous" node (which was next before swap)
            curr = curr.prev  
        
        return new_head
