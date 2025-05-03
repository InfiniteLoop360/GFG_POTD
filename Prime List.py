class Solution:
    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def nearest_prime(self, n):
        if self.is_prime(n):
            return n

        prev = n - 1
        next_ = n + 1

        while True:
            if prev >= 2 and self.is_prime(prev):
                return prev
            if self.is_prime(next_):
                return next_
            prev -= 1
            next_ += 1

    def primeList(self, head):
        temp = head
        while temp:
            temp.val = self.nearest_prime(temp.val)
            temp = temp.next
        return head
