'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        if not head or not head.next:
            return 0
        
        slow = head
        fast = head

        # Step 1: Detect cycle using Floyd’s algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # Cycle detected
                # Step 2: Count loop length
                count = 1
                curr = slow.next
                while curr != slow:
                    count += 1
                    curr = curr.next
                return count

        # No cycle
        return 0
