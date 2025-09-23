from collections import deque

class Solution:
    def reverseQueue(self, q):
        stack = []
        
        # Step 1: Push all elements into stack
        while q:
            stack.append(q.popleft())
        
        # Step 2: Pop from stack and add back to queue
        while stack:
            q.append(stack.pop())
        
        return q
