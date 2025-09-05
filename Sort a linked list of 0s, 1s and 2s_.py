'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        if not head or not head.next:
            return head

        # Dummy heads and tails
        zeroD = Node(-1)
        oneD = Node(-1)
        twoD = Node(-1)

        zero = zeroD
        one = oneD
        two = twoD

        # Partition nodes into 3 lists
        curr = head
        while curr:
            if curr.data == 0:
                zero.next = curr
                zero = zero.next
            elif curr.data == 1:
                one.next = curr
                one = one.next
            else:
                two.next = curr
                two = two.next
            curr = curr.next

        # Connect the three lists
        zero.next = oneD.next if oneD.next else twoD.next
        one.next = twoD.next
        two.next = None

        # Return the correct new head
        return zeroD.next if zeroD.next else (oneD.next if oneD.next else twoD.next)
