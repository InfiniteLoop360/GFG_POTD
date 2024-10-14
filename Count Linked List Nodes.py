'''
Count Linked List Nodes

Given a singly linked list. The task is to find the length of the linked list, where length is defined as the number of nodes in the linked list.

Examples :

Input: LinkedList : 1->2->3->4->5

Output: 5
Explanation: Count of nodes in the linked list is 5, which is its length.
Input: LinkedList : 2->4->6->7->5->1->0
 
Output: 7
Explanation: Count of nodes in the linked list is 7. Hence, the output is 7.
Expected Time Complexity: O(n)
Expected Auxilliary Space: O(1)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
To solve the problem of counting the number of nodes in a singly linked list, we can traverse the linked list and increment a counter at each node until we reach the end of the list. This approach ensures a time complexity of \(O(n)\), where \(n\) is the number of nodes in the list.

### Approach:

1. Start from the `head` of the linked list.
2. Initialize a counter variable to zero.
3. Traverse the linked list:
   - For each node, increment the counter.
   - Move to the next node.
4. Stop when we reach the end of the list (i.e., the next node is `None`).
5. Return the counter, which will be the number of nodes in the linked list.

'''
# Node class to represent each node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None

# Solution class to provide the method to count nodes
class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        # Initialize count to 0
        count = 0
        # Initialize current node as head
        current = head
        
        # Traverse the linked list until current is None
        while current:
            count += 1  # Increment count
            current = current.next  # Move to the next node
        
        # Return the final count
        return count

# Example usage:
# Create a linked list with 5 nodes: 1 -> 2 -> 3 -> 4 -> 5
ll = LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)
ll.head.next.next.next.next = Node(5)

# Create a solution object and find the count of nodes
solution = Solution()
result = solution.getCount(ll.head)
print(result)  # Output: 5

'''

1. **Node Class**: The `Node` class defines a single node in the linked list. Each node contains `data` and a pointer to the next node (`next`).
2. **LinkedList Class**: This class initializes a linked list with `head` (and potentially `tail`) pointers.
3. **Solution Class**:
   - The `getCount` function iterates through the list from `head`, counting each node, and returns the total count.
4. **Example**:
   - A linked list `1 -> 2 -> 3 -> 4 -> 5` is created.
   - The `getCount` method is called on the `head` node, and it returns `5`, the number of nodes.

### Time Complexity:
- **Time Complexity**: \(O(n)\), where \(n\) is the number of nodes in the linked list.
- **Space Complexity**: \(O(1)\), since no extra space is used apart from the counter variable.
'''
