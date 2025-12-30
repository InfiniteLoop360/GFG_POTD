class Solution:
    def addTwoLists(self, head1, head2):
        
        # Helper function to reverse a linked list
        def reverse(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        # Reverse both lists
        head1 = reverse(head1)
        head2 = reverse(head2)
        
        carry = 0
        dummy = Node(0)
        curr = dummy
        
        # Add both numbers
        while head1 or head2 or carry:
            val1 = head1.data if head1 else 0
            val2 = head2.data if head2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            
            curr.next = Node(total % 10)
            curr = curr.next
            
            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next
        
        # Reverse result list
        result = reverse(dummy.next)
        
        # Remove leading zeros
        while result and result.data == 0 and result.next:
            result = result.next
        
        return result
