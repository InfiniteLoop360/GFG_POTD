class Solution:
    # Function to remove a loop in the linked list.
    def removeLoop(self, head):
        if not head or not head.next:
            return
        
        # Detecting the loop using Floyd's Cycle Detection Algorithm
        slow, fast = head, head
        loop_exists = False
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # Loop detected
                loop_exists = True
                break
        
        # If no loop exists, return
        if not loop_exists:
            return
        
        # Find the start of the loop
        slow = head
        if slow == fast:  # Special case: the loop starts at the head
            while fast.next != slow:
                fast = fast.next
        else:
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next
        
        # Break the loop
        fast.next = None
