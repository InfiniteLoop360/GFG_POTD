class Solution:
    def cloneLinkedList(self, head):
        if not head:
            return None

        # Step 1: Create a new node for each node in the original list and insert it between the original nodes
        current = head
        while current:
            new_node = Node(current.data)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        # Step 2: Copy the random pointers for the newly created nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Separate the cloned list from the original list
        current = head
        clone_head = head.next
        clone_current = clone_head
        while current:
            current.next = current.next.next
            if clone_current.next:
                clone_current.next = clone_current.next.next
            current = current.next
            clone_current = clone_current.next

        return clone_head
