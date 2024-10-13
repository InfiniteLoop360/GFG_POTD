'''
Delete Alternate Nodes
Given a Singly Linked List, Delete all alternate nodes of the list ie delete all the nodes present in even positions.

Examples :

Input: LinkedList: 1->2->3->4->5->6
 
Output: 1->3->5

Explanation: Deleting alternate nodes ie 2, 4, 6 results in the linked list with elements 1->3->5.
Input: LinkedList: 99->59->42->20
 
Output: 99->42
 
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Let's go through a **detailed approach** to solve the problem of deleting alternate nodes in a **singly linked list**:

### Problem Recap:
Given a singly linked list, we need to delete all nodes at **even positions**, effectively keeping the nodes at odd positions only. The node at position 1 (head) is considered odd, position 2 is even, and so on. 

For example:
- **Input**: `1 -> 2 -> 3 -> 4 -> 5 -> 6`
- **Output**: `1 -> 3 -> 5`

### Approach:

1. **Understanding the List Structure**:
   - A singly linked list consists of nodes where each node contains two elements: **data** (the value of the node) and **next** (a pointer to the next node in the list).
   - We are given access to the **head** node (the starting point of the list). 

2. **Problem Clarification**:
   - We need to remove all the nodes at even positions. This means that for each node `n1`, `n2`, `n3`, etc., we will remove `n2`, `n4`, `n6`, and so on. 
   - The goal is to update the `next` pointer of the node at an odd position to point to the node that comes after the node at an even position.

3. **Core Idea**:
   - Traverse the list using a **current** pointer.
   - For each node, we will:
     - Delete the node immediately after the current node (`current.next`), which is the node in the **even position**.
     - Update the `next` pointer of the current node to skip the next node and point to the node after it (`current.next = current.next.next`).
     - Move the `current` pointer two steps forward (to the next valid odd-position node) and continue this process until the end of the list.

4. **Algorithm**:
   - **Step 1**: Initialize a pointer `current` to the `head` of the list.
   - **Step 2**: Traverse the list while `current` and `current.next` are not `None` (this ensures there is a node to delete):
     - Set `current.next = current.next.next` to bypass the next (even-positioned) node.
     - Move `current` to the next odd-positioned node (`current = current.next`).
   - **Step 3**: Stop when you reach the end of the list (`current` becomes `None`).

'''
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def deleteAlt(self, head):
        if head is None:
            return None
        
        current = head
        while current and current.next:
            # Skip the next node
            current.next = current.next.next
            # Move to the next node
            current = current.next

# Function to print the linked list
def printList(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()
'''
### Explanation of the Code:
1. **Node Class**:
   - This is a simple class representing a node in the linked list. It has two attributes: `data` (to store the value) and `next` (a reference to the next node).
   
2. **deleteAlt Function**:
   - **Line 7**: If the `head` is `None` (i.e., the list is empty), we immediately return `None` because there's no node to process.
   - **Line 10**: The `current` pointer is initialized to the head of the list. This pointer will be used to traverse through the list.
   - **Line 13**: The `while` loop iterates as long as there are nodes available. Specifically, we need `current` and `current.next` to be non-`None` to ensure there's a node to skip.
   - **Line 15**: We set `current.next` to `current.next.next` to bypass (or delete) the next node (which is at the even position).
   - **Line 17**: After bypassing the node, we move `current` to the next valid node (the node now pointed by `current.next`). This ensures we always process the odd-positioned nodes.

### Example Walkthrough:

**Example 1**: `1 -> 2 -> 3 -> 4 -> 5 -> 6`
- **Initial List**: `1 -> 2 -> 3 -> 4 -> 5 -> 6`
- **Step 1**: Start at `current = 1`. Set `1.next` to `3` (skipping node `2`), resulting in:  
  `1 -> 3 -> 4 -> 5 -> 6`
- **Step 2**: Move `current` to `3`. Set `3.next` to `5` (skipping node `4`), resulting in:  
  `1 -> 3 -> 5 -> 6`
- **Step 3**: Move `current` to `5`. Set `5.next` to `None` (skipping node `6`), resulting in:  
  `1 -> 3 -> 5`
- **Final List**: `1 -> 3 -> 5`

**Example 2**: `99 -> 59 -> 42 -> 20`
- **Initial List**: `99 -> 59 -> 42 -> 20`
- **Step 1**: Start at `current = 99`. Set `99.next` to `42` (skipping node `59`), resulting in:  
  `99 -> 42 -> 20`
- **Step 2**: Move `current` to `42`. Set `42.next` to `None` (skipping node `20`), resulting in:  
  `99 -> 42`
- **Final List**: `99 -> 42`

### Time and Space Complexity:
- **Time Complexity**: O(n), where `n` is the number of nodes in the linked list. We traverse each node once, and skipping the next node takes constant time (O(1)).
- **Space Complexity**: O(1), since we're using a constant amount of extra space regardless of the size of the input list.

This solution is optimal in both time and space complexity for this problem.
'''
