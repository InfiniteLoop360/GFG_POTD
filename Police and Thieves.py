from collections import deque

class Solution:
    def catchThieves(self, arr, k):
        police = deque()
        thief = deque()
        n = len(arr)
        count = 0

        for i in range(n):
            if arr[i] == 'P':
                police.append(i)
            elif arr[i] == 'T':
                thief.append(i)

        while police and thief:
            if abs(police[0] - thief[0]) <= k:
                count += 1
                police.popleft()
                thief.popleft()
            elif police[0] < thief[0]:
                police.popleft()
            else:
                thief.popleft()

        return count
