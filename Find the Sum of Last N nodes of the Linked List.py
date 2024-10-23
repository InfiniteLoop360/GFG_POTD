class Solution:
    def sumOfLastN_Nodes(self, head, n):
        # Initialize two pointers
        first = head
        second = head
        
        # Move the first pointer n steps ahead
        for _ in range(n):
            if first:
                first = first.next
        
        # Move both pointers until the first pointer reaches the end
        while first:
            first = first.next
            second = second.next
        
        # Sum the last n nodes
        sum_last_n = 0
        while second:
            sum_last_n += second.data  # Use 'data' instead of 'val'
            second = second.next
        
        return sum_last_n
