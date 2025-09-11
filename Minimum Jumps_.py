class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n == 0:
            return -1
        if n == 1:
            return 0
        # If the first element is 0, we can't move anywhere (unless n==1)
        if arr[0] == 0:
            return -1

        jumps = 0
        current_end = 0   # end of range reachable with 'jumps' jumps
        farthest = 0      # farthest index reachable by exploring the current range

        # We iterate to n-2 because when we reach or pass n-1 we can stop early
        for i in range(n - 1):
            # Update the farthest we can reach from this index
            farthest = max(farthest, i + arr[i])

            # If we've reached the end of the current range, we must make a jump
            if i == current_end:
                # If farthest does not advance, we are stuck
                if farthest <= i:
                    return -1
                jumps += 1
                current_end = farthest
                # If we can already reach the last index, stop early
                if current_end >= n - 1:
                    break

        return jumps
