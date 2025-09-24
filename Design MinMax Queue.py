from collections import deque

class SpecialQueue:
    def __init__(self):
        self.mainQueue = deque()
        self.minDeque = deque()
        self.maxDeque = deque()

    def enqueue(self, x):
        # Add to main queue
        self.mainQueue.append(x)

        # Maintain minDeque (increasing order)
        while self.minDeque and self.minDeque[-1] > x:
            self.minDeque.pop()
        self.minDeque.append(x)

        # Maintain maxDeque (decreasing order)
        while self.maxDeque and self.maxDeque[-1] < x:
            self.maxDeque.pop()
        self.maxDeque.append(x)

    def dequeue(self):
        if not self.mainQueue:
            return
        val = self.mainQueue.popleft()

        if self.minDeque and self.minDeque[0] == val:
            self.minDeque.popleft()
        if self.maxDeque and self.maxDeque[0] == val:
            self.maxDeque.popleft()

    def getFront(self):
        return self.mainQueue[0] if self.mainQueue else None

    def getMin(self):
        return self.minDeque[0] if self.minDeque else None

    def getMax(self):
        return self.maxDeque[0] if self.maxDeque else None
