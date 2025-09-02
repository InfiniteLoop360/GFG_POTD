'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def swapKth(self, head, k):
        # Step 1: find length of list
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        
        # Step 2: invalid cases
        if k > n:
            return head
        if (2*k - 1) == n:  # same node
            return head
        
        # Step 3: find kth node from start
        x_prev, x = None, head
        for i in range(1, k):
            x_prev = x
            x = x.next
        
        # Step 4: find kth node from end
        y_prev, y = None, head
        for i in range(1, n - k + 1):
            y_prev = y
            y = y.next
        
        # Step 5: swap
        if x_prev:
            x_prev.next = y
        if y_prev:
            y_prev.next = x
        
        # Swap next pointers
        x.next, y.next = y.next, x.next
        
        # Step 6: update head if needed
        if k == 1:
            head = y
        if k == n:
            head = x
        
        return head
