/*
### XOR Linked List: Detailed Solution Approach and Explanation

An XOR linked list is a memory-efficient version of a doubly linked list that uses the XOR bitwise operation to store only one pointer per node, which represents the XOR of the addresses of the previous and next nodes. This reduces the memory footprint since you only store one pointer instead of two. However, it introduces complexity when navigating the list.

#### Key Concepts:

1. **Node Structure**:
   - Each node contains:
     - `data`: The value stored in the node.
     - `npx`: A pointer that holds the XOR of the addresses of the previous and next nodes.
   - This means you can traverse the list forward and backward using the XOR operation.

2. **XOR Operation**:
   - The XOR of two pointers allows you to determine the next or previous node in the list without needing separate pointers.
   - `XOR(a, b) = a ^ b`: This operation returns a value where the bits are set to `1` if the corresponding bits of `a` and `b` are different.

3. **Memory Efficiency**:
   - Traditional doubly linked lists require two pointers per node, whereas XOR linked lists only need one, reducing the overall memory used for pointers.

### Approach:

#### 1. **Insert Function**:
- The `insert` function adds a new node at the beginning of the list.

**Steps**:
- **Create a New Node**: Allocate a new node with the given data.
- **Check for Empty List**: If the list is empty (i.e., `head` is `nullptr`), the new node becomes the head.
- **Update New Node's `npx`**: Set the new node’s `npx` to point to the current head (i.e., the next node is the current head).
- **Update Head Node's `npx`**: Update the current head's `npx` to reflect the new node.
  - The `npx` of the head node is updated as:
  ```cpp
  head->npx = XOR(new_node, head->npx);
  ```
  This effectively links the new node with the current head.
- **Return New Head**: The new node now becomes the head of the list.

#### 2. **GetList Function**:
- The `getList` function retrieves the data from the linked list as a vector.

**Steps**:
- **Initialize Variables**: Start with an empty vector to store node data, set `current` to the head, and `prev` to `nullptr`.
- **Traversal**: While `current` is not `nullptr`, perform the following:
  - **Store Data**: Append the data from the `current` node to the result vector.
  - **Calculate Next Node**: Use the `XOR` of the `prev` pointer and the `current->npx` to find the address of the next node.
    ```cpp
    Node* next = XOR(prev, current->npx);
    ```
  - **Update Pointers**: Move `prev` to `current`, and `current` to `next`.
- **Return Result**: Once the traversal is complete, return the vector containing the node data.

*/

#include <iostream>
#include <vector>

using namespace std;

// Node structure definition
struct Node {
    int data;      // Data stored in the node
    Node* npx;    // XOR of the next and previous node addresses
    Node(int data) : data(data), npx(nullptr) {} // Constructor to initialize node
};

// XOR function to get XOR of two pointers
Node* XOR(Node* a, Node* b) {
    return (Node*)((uintptr_t)(a) ^ (uintptr_t)(b)); // Cast to uintptr_t for XOR operation
}

// Insert function to add a new node at the beginning of the list
struct Node* insert(struct Node* head, int data) {
    Node* new_node = new Node(data); // Create a new node

    if (head == nullptr) { // If the list is empty
        return new_node; // New node becomes the head
    }

    // Update the new node's npx to point to the current head
    new_node->npx = head; // The next node will be the current head
    // Update the current head's npx to include the new node
    head->npx = XOR(new_node, head->npx); // Update head's npx
    return new_node; // Return the new head
}

// Function to retrieve the list as a vector of integers
vector<int> getList(struct Node* head) {
    vector<int> result; // Vector to store the node data
    Node* current = head; // Start with the head of the list
    Node* prev = nullptr; // Previous node is initially null

    while (current != nullptr) { // Traverse until the end of the list
        result.push_back(current->data); // Add the current node's data to the result
        Node* next = XOR(prev, current->npx); // Get the next node using XOR
        prev = current; // Move prev to current
        current = next; // Move to the next node
    }

    return result; // Return the result vector
}

// Function to print the list for testing
void printList(struct Node* head) {
    vector<int> list = getList(head); // Get the list data
    for (int val : list) { // Print each element in the list
        cout << val << " ";
    }
    cout << endl; // New line after printing the list
}

// Main function for demonstration
int main() {
    struct Node* head = nullptr; // Initialize head to null
    
    // Insert data into the XOR linked list
    head = insert(head, 10);
    head = insert(head, 3);
    head = insert(head, 7);
    head = insert(head, 4);
    head = insert(head, 5);
    head = insert(head, 9);
    
    // Print the linked list
    cout << "Forward: ";
    printList(head); // Call print function to display the list
    
    return 0; // Indicate successful completion
}

/*
### Complexity Analysis:

- **Time Complexity**:
  - The `insert` operation is \(O(1)\) since it only involves updating a few pointers.
  - The `getList` operation is \(O(n)\), where \(n\) is the number of nodes, because it requires traversing the entire list once.

- **Space Complexity**:
  - The space complexity for the `insert` operation is \(O(1)\) as it only requires a fixed amount of additional space.
  - The `getList` operation uses \(O(n)\) space to store the result in a vector.

### Conclusion:
The XOR linked list is a powerful data structure that effectively reduces memory usage for storing pointers while introducing complexity in pointer manipulation. Understanding how to implement and navigate this structure is essential for optimizing space in systems where memory usage is critical.
  */
