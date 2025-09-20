class Solution:
    def longestSubarray(self, arr):
        """
        Return the length of the longest subarray such that every element in that subarray
        is ≤ (length of the subarray).
        """
        n = len(arr)
        if n == 0:
            return 0

        # Values > n can never be part of a valid subarray, clamp them to n+1
        vals = [v if v <= n else n+1 for v in arr]

        # pairs sorted by value: (value, index)
        pairs = sorted((vals[i], i) for i in range(n))

        parent = list(range(n))
        size = [0] * n
        active = [False] * n

        def find(x):
            # path compression
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return size[ra]
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
            return size[ra]

        p = 0                # pointer into pairs
        max_seg = 0
        ans = 0

        # for each possible length k
        for k in range(1, n + 1):
            # activate all indices whose value <= k
            while p < n and pairs[p][0] <= k:
                _, idx = pairs[p]
                active[idx] = True
                parent[idx] = idx
                size[idx] = 1
                # union with left neighbor if active
                if idx - 1 >= 0 and active[idx - 1]:
                    union(idx, idx - 1)
                # union with right neighbor if active
                if idx + 1 < n and active[idx + 1]:
                    union(idx, idx + 1)
                # update max segment length
                max_seg = max(max_seg, size[find(idx)])
                p += 1

            if max_seg >= k:
                ans = k

        return ans
