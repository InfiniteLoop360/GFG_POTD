class GfG {
    // Helper function to get the tail of the linked list
    private static Node getTail(Node head) {
        while (head != null && head.next != null) {
            head = head.next;
        }
        return head;
    }

    // Partition function that rearranges the nodes based on the pivot
    private static Node partition(Node head, Node end, Node[] newHead, Node[] newEnd) {
        Node pivot = end;
        Node prev = null, curr = head, tail = pivot;

        // Iterate through the list and rearrange nodes
        while (curr != pivot) {
            if (curr.data < pivot.data) {
                if (newHead[0] == null) {
                    newHead[0] = curr;
                }
                prev = curr;
                curr = curr.next;
            } else {
                if (prev != null) {
                    prev.next = curr.next;
                }
                Node tmp = curr.next;
                curr.next = null;
                tail.next = curr;
                tail = curr;
                curr = tmp;
            }
        }

        // Update newEnd to the current tail
        newEnd[0] = tail;

        // Return pivot as new head if new head is null
        if (newHead[0] == null) {
            newHead[0] = pivot;
        }
        return pivot;
    }

    // Main quicksort recursive function
    private static Node quickSortRecur(Node head, Node end) {
        if (head == null || head == end) {
            return head;
        }

        Node[] newHead = { null }, newEnd = { null };

        Node pivot = partition(head, end, newHead, newEnd);

        if (newHead[0] != pivot) {
            Node temp = newHead[0];
            while (temp.next != pivot) {
                temp = temp.next;
            }
            temp.next = null;

            newHead[0] = quickSortRecur(newHead[0], temp);

            temp = getTail(newHead[0]);
            temp.next = pivot;
        }

        pivot.next = quickSortRecur(pivot.next, newEnd[0]);

        return newHead[0];
    }

    public static Node quickSort(Node node) {
        Node tail = getTail(node);
        return quickSortRecur(node, tail);
    }
}
