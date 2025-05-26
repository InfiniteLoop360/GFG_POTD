class Solution {
  sortedInsert(head, data) {
    // Create the new node as a plain object
    const newNode = { data: data, next: null };

    // If the list is empty, the new node points to itself and becomes the head
    if (!head) {
      newNode.next = newNode;
      return newNode;
    }

    let current = head;

    // Traverse the circular list to find the correct insertion position
    while (true) {
      // Check if the current node is the right place to insert the new node
      if (
        (current.data <= data && data <= current.next.data) ||
        // If we've looped back to the head, insert here (end of list)
        current.next === head
      ) {
        break;
      }

      // Move to the next node in the list
      current = current.next;
    }

    // Insert the new node after the current node
    newNode.next = current.next;
    current.next = newNode;

    // If the new node's data is smaller than the head's data, update the head to the new node
    if (data < head.data) {
      head = newNode;
    }

    // Return the updated head of the list
    return head;
  }
}
