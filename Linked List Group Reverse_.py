"""
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""

class Solution:
    def reverseKGroup(self, head, k):
        if head is None:
            return None
        
        # Step 1: Check if at least k nodes exist
        count = 0
        temp = head
        while temp and count < k:
            temp = temp.next
            count += 1
        
        # If we have less than k nodes, we still reverse (as per problem statement)
        if count < k:
            return self.reversePartial(head, count)
        
        # Step 2: Reverse exactly k nodes
        prev = None
        curr = head
        nxt = None
        count = 0
        while curr and count < k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count += 1
        
        # Step 3: Connect rest (recursive call for remaining list)
        if nxt:
            head.next = self.reverseKGroup(nxt, k)
        
        # prev is new head after reversal
        return prev

    # Helper to reverse leftover nodes (< k size)
    def reversePartial(self, head, size):
        prev = None
        curr = head
        nxt = None
        count = 0
        while curr and count < size:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count += 1
        return prev
