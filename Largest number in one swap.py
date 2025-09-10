class Solution:
    def largestSwap(self, s: str) -> str:
        # Convert to list for easy swapping
        arr = list(s)
        n = len(arr)

        # last[d] = last index where digit d (as an int) appears
        last = [-1] * 10
        for i, ch in enumerate(arr):
            last[ord(ch) - ord('0')] = i

        # For each position i from left to right, try to find a bigger digit
        for i in range(n):
            cur = ord(arr[i]) - ord('0')
            # look for bigger digits from 9 down to cur+1
            for d in range(9, cur, -1):
                j = last[d]
                if j > i:
                    # swap arr[i] and arr[j], return result
                    arr[i], arr[j] = arr[j], arr[i]
                    return ''.join(arr)
        # nothing to improve
        return s
