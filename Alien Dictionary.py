from collections import defaultdict, deque

class Solution:
    def findOrder(words):
        # Step 1: Build the graph
        adj = defaultdict(set)
        in_degree = defaultdict(int)
        all_chars = set()

        # Initialize all characters
        for word in words:
            for ch in word:
                all_chars.add(ch)

        # Build graph from adjacent word pairs
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            found_order = False

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    found_order = True
                    break

            # Edge case: prefix situation like ["abc", "ab"] → invalid
            if not found_order and len(w1) > len(w2):
                return ""

        # Step 2: Topological Sort using Kahn’s Algorithm
        q = deque()
        for ch in all_chars:
            if in_degree[ch] == 0:
                q.append(ch)

        result = []

        while q:
            current = q.popleft()
            result.append(current)

            for neighbor in adj[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        # If all characters are included, return result
        if len(result) == len(all_chars):
            return ''.join(result)
        else:
            return ""  # Cycle detected or incomplete ordering
