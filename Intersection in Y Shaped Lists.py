class Solution:
    def intersectPoint(self, head1, head2):
        if not head1 or not head2:
            return None
        
        p1, p2 = head1, head2
        
        while p1 != p2:
            p1 = p1.next if p1 else head2
            p2 = p2.next if p2 else head1
        
        # Return the NODE, not the value
        return p1
