from collections import deque, defaultdict

class Solution:
    def minTime(self, root, target):
        # Step 1: Map every node to its parent and find the target node
        parent_map = {}
        target_node = None

        def map_parents(node, parent=None):
            nonlocal target_node
            if not node:
                return
            if node.data == target:
                target_node = node
            parent_map[node] = parent
            map_parents(node.left, node)
            map_parents(node.right, node)

        map_parents(root)

        # Step 2: BFS from the target node
        visited = set()
        queue = deque()
        queue.append(target_node)
        visited.add(target_node)

        time = -1  # Starts at -1 so first level becomes 0 sec

        while queue:
            size = len(queue)
            for _ in range(size):
                current = queue.popleft()
                # Check left, right, and parent
                for neighbor in (current.left, current.right, parent_map.get(current)):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            time += 1  # Increment time after each level

        return time
