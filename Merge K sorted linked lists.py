from heapq import heappush, heappop

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def mergeKLists(self, arr):
        min_heap = []
        
        # Push the head of each list into the heap
        for idx, node in enumerate(arr):
            if node:
                heappush(min_heap, (node.data, idx, node))  # Use node.data instead of node.val
        
        dummy = Node(-1)
        curr = dummy
        
        while min_heap:
            data, idx, node = heappop(min_heap)  # Get the smallest element
            curr.next = node
            curr = curr.next
            if node.next:
                heappush(min_heap, (node.next.data, idx, node.next))  # Push next node from the same list
        
        return dummy.next  # Return head of the merged linked list
