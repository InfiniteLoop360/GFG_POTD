'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def mergeSort(self, head):
        # Base case: if 0 or 1 element
        if not head or not head.next:
            return head

        # Step 1: Split the linked list into halves
        mid = self.getMiddle(head)
        next_to_mid = mid.next
        mid.next = None  # break into two halves

        # Step 2: Sort both halves
        left = self.mergeSort(head)
        right = self.mergeSort(next_to_mid)

        # Step 3: Merge sorted halves
        sorted_list = self.sortedMerge(left, right)
        return sorted_list

    def getMiddle(self, head):
        # Fast & slow pointer to find middle
        if not head:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sortedMerge(self, a, b):
        # Merge two sorted lists
        if not a:
            return b
        if not b:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result
