class Solution:
    def countNodesInLoop(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Loop detected
                return self.countLoopLength(slow)
        
        return 0  # No loop

    def countLoopLength(self, node_in_loop):
        count = 1
        temp = node_in_loop.next
        while temp != node_in_loop:
            count += 1
            temp = temp.next
        return count
