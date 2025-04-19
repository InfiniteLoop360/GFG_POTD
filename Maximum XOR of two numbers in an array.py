class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        node = self.root
        for i in reversed(range(32)):  # 31 to 0 (since numbers can go up to 10^6 ~ 20 bits, 32 to be safe)
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
    
    def find_max_xor(self, num):
        node = self.root
        max_xor = 0
        for i in reversed(range(32)):
            bit = (num >> i) & 1
            opposite_bit = 1 - bit
            if opposite_bit in node.children:
                max_xor |= (1 << i)
                node = node.children[opposite_bit]
            else:
                node = node.children.get(bit, node)
        return max_xor

class Solution:
    def maxXor(self, arr):
        trie = Trie()
        max_xor = 0
        trie.insert(arr[0])
        
        for i in range(1, len(arr)):
            max_xor = max(max_xor, trie.find_max_xor(arr[i]))
            trie.insert(arr[i])
        
        return max_xor
