class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True  # An empty list or single node list is a palindrome
        
        # Step 1: Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        second_half = self.reverseList(slow)
        first_half = head
        
        # Step 3: Compare the first half and the reversed second half
        while second_half:
            if first_half.data != second_half.data:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        return True

    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

# Utility function to create a linked list from a list of values
def createLinkedList(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head
