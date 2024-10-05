'''
Given a Circular Linked List. The task is to delete the given node, key in the circular linked list, and reverse the circular linked list.

Note:

You don't have to print anything, just return the head of the modified list in each function.
Nodes may consist of Duplicate values.
The key may or may not be present.

Example:

Input: Linked List: 2->5->7->8->10, key = 8
Output: 10->7->5->2 
Explanation:
After deleting 8 from the given circular linked list, it has elements as 2, 5, 7, 10. Now, reversing this list will result in 10, 7, 5, 2

Input: Linked List: 1->7->8->10, key = 8
Output: 10->7->1
Explanation: 
After deleting 8 from the given circular linked list, it has elements as 1, 7,10. Now, reversing this list will result in 10, 7, 1.

Expected Time Complexity: O(n)
Expected Auxillary Space: O(1)
'''

class Solution:
    # Function to reverse a circular linked list
    def reverse(self, head):
        if not head or head.next == head:
            return head
        
        prev = None
        curr = head
        last = head
        
        # Find the last node
        while last.next != head:
            last = last.next
        
        while curr.next != head:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        curr.next = prev
        head.next = curr
        return curr
    
    # Function to delete a node from the circular linked list
    def deleteNode(self, head, key):
        if not head:
            return None
        
        # If head is to be deleted
        if head.data == key:
            # If it's the only node in the list
            if head.next == head:
                return None
            
            # Find the last node
            last = head
            while last.next != head:
                last = last.next
            
            # Move head and adjust the last node's next pointer
            last.next = head.next
            head = head.next
            return head
        
        # Traverse to find the node to delete
        curr = head
        while curr.next != head and curr.next.data != key:
            curr = curr.next
        
        # If node is found, delete it
        if curr.next.data == key:
            curr.next = curr.next.next
        
        return head

# Utility function to print the circular linked list
def printList(head):
    if not head:
        return
    temp = head
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == head:
            break
    print()

# Helper function to create a circular linked list from a list
def createCircularLinkedList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        curr.next = new_node
        curr = new_node
    curr.next = head
    return head
