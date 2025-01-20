# Node class is already defined
class Solution:
    def sortedMerge(self, head1, head2):
        # Create a dummy node to simplify the merging process
        dummy = Node(0)
        tail = dummy

        # Merge the two lists
        while head1 and head2:
            if head1.data <= head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        # Attach the remaining nodes from either list
        if head1:
            tail.next = head1
        if head2:
            tail.next = head2

        # Return the head of the merged list
        return dummy.next
