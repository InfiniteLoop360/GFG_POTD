class Solution:
    def rotate(self, head, k):
        # If the list is empty, has only one node, or no rotation is needed
        if not head or not head.next or k == 0:
            return head

        # Step 1: Calculate the length of the linked list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Normalize k to avoid unnecessary rotations
        k = k % length
        if k == 0:
            return head

        # Step 3: Find the new head and new tail after k rotations
        # Traverse the list to find the (k-1)th node
        new_tail = head
        for _ in range(k - 1):
            new_tail = new_tail.next
        
        # The new head is the next node after the new tail
        new_head = new_tail.next
        
        # Step 4: Update the connections
        new_tail.next = None  # Break the link
        tail.next = head  # Connect the old tail to the old head
        
        return new_head
