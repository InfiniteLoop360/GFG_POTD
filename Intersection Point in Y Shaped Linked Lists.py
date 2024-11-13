def intersetPoint(head1, head2):
    # Step 1: Get the lengths of both linked lists
    def getLength(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    len1, len2 = getLength(head1), getLength(head2)
    
    # Step 2: Align the starting points of both lists
    # Determine the longer and shorter list
    if len1 > len2:
        longer, shorter = head1, head2
        diff = len1 - len2
    else:
        longer, shorter = head2, head1
        diff = len2 - len1
    
    # Advance the pointer of the longer list by 'diff' nodes
    for _ in range(diff):
        longer = longer.next
    
    # Step 3: Traverse both lists in tandem to find the intersection point
    while longer and shorter:
        if longer == shorter:
            return longer.data
        longer = longer.next
        shorter = shorter.next
    
    # If no intersection is found
    return -1
