'''
Split Linked List Alternatingly

Given a singly linked list's head. Your task is to complete the function alternatingSplitList() that splits the given linked list into two smaller lists. The sublists should be made from alternating elements from the original list.
Note: 

The sublist should be in the order with respect to the original list.
Your have to return an array containing the both sub-linked lists.
Examples:

Input: LinkedList = 0->1->0->1->0->1
Output: 0->0->0 , 1->1->1
Explanation: After forming two sublists of the given list as required, we have two lists as: 0->0->0 and 1->1->1.

Input: LinkedList = 2->5->8->9->6
Output: 2->8->6 , 5->9
Explanation: After forming two sublists of the given list as required, we have two lists as: 2->8->6 and 5->9.
Input: LinkedList: 7 
Output: 7 , <empty linked list>
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
To split a singly linked list into two smaller linked lists by alternating nodes, you can iterate through the original list and distribute the nodes into two new lists. Here's how you can implement this in Python:

### Implementation Steps:
1. Initialize two new linked lists (`list1` and `list2`).
2. Use a pointer to traverse the original linked list.
3. For every node, based on its position (even or odd), append it to either `list1` or `list2`.
4. Finally, return both lists.

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def alternatingSplitList(self, head):
        # Create two dummy nodes for the two new lists
        list1_head = Node(0)  # Dummy head for list1
        list2_head = Node(0)  # Dummy head for list2
        
        list1_curr = list1_head  # Pointer for list1
        list2_curr = list2_head  # Pointer for list2
        
        current = head  # Pointer for traversing the original list
        index = 0  # To keep track of the position (even or odd)
        
        while current:
            if index % 2 == 0:
                # Even index: add to list1
                list1_curr.next = current
                list1_curr = list1_curr.next
            else:
                # Odd index: add to list2
                list2_curr.next = current
                list2_curr = list2_curr.next
            
            current = current.next  # Move to the next node
            index += 1
        
        # End the lists
        list1_curr.next = None
        list2_curr.next = None
        
        # Return the next of the dummy heads, which is the actual head of the new lists
        return [list1_head.next, list2_head.next]
'''

### Explanation:
- **Node Class**: A simple node class to represent each element in the linked list.
- **Dummy Heads**: Using dummy nodes (`list1_head` and `list2_head`) helps in simplifying the addition of nodes to `list1` and `list2`.
- **Current Pointer**: This pointer traverses the original list. Depending on whether the index is even or odd, it appends the current node to `list1` or `list2`.
- **Finalizing Lists**: At the end of the loop, both new lists are terminated by setting their `next` pointers to `None`.
- **Return Value**: The function returns a list containing the heads of the two new lists.
'''
