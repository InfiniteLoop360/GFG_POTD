class Solution:
    class TrieNode:
        def __init__(self):
            self.child = [None, None]
            self.count = 0

    def insert(self, root, num):
        node = root
        for b in range(15, -1, -1):          # 16 bits because arr[i], k ≤ 50000
            bit = (num >> b) & 1
            if not node.child[bit]:
                node.child[bit] = self.TrieNode()
            node = node.child[bit]
            node.count += 1

    def query(self, root, num, k):
        node = root
        ans = 0
        for b in range(15, -1, -1):
            if not node:
                break

            x = (num >> b) & 1      # bit of num
            y = (k >> b) & 1        # bit of k

            if y == 1:
                # If k-bit is 1 → we can take all numbers where trie-bit == x
                if node.child[x]:
                    ans += node.child[x].count
                # Move to the opposite branch for strict comparison
                node = node.child[1 - x]
            else:
                # If k-bit is 0 → must take only numbers where trie-bit == x
                node = node.child[x]

        return ans

    def cntPairs(self, arr, k):
        root = self.TrieNode()
        count = 0

        for num in arr:
            count += self.query(root, num, k)
            self.insert(root, num)

        return count
