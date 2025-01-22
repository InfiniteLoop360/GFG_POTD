class Solution:
    def addTwoLists(self, num1, num2):
        # Helper function to reverse a linked list
        def reverseList(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        # Helper function to remove leading zeros from the list
        def removeLeadingZeros(head):
            while head and head.data == 0:
                head = head.next
            return head if head else Node(0)

        # Reverse the input lists
        num1 = reverseList(num1)
        num2 = reverseList(num2)

        # Initialize carry and result linked list
        carry = 0
        dummy = Node(0)
        current = dummy

        # Add the two numbers represented by the reversed lists
        while num1 or num2 or carry:
            sum_value = carry
            if num1:
                sum_value += num1.data
                num1 = num1.next
            if num2:
                sum_value += num2.data
                num2 = num2.next

            # Calculate carry and current digit
            carry = sum_value // 10
            current.next = Node(sum_value % 10)
            current = current.next

        # Reverse the result list and remove leading zeros
        result = reverseList(dummy.next)
        result = removeLeadingZeros(result)

        return result
