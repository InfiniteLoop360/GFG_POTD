class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, s, start):
        """ Returns list of possible end indices where words end """
        node = self.root
        ends = []
        for i in range(start, len(s)):
            if s[i] not in node.children:
                break
            node = node.children[s[i]]
            if node.is_end:
                ends.append(i + 1)  # Store end index (1-based)
        return ends

class Solution:
    def wordBreak(self, s, dictionary):
        trie = Trie()
        for word in dictionary:
            trie.insert(word)  # Insert all words into Trie
        
        n = len(s)
        memo = {}  # Memoization dictionary

        def dfs(start):
            if start == n:
                return True
            if start in memo:
                return memo[start]

            for end in trie.search(s, start):
                if dfs(end):  # If we find a valid segmentation
                    memo[start] = True
                    return True
            
            memo[start] = False
            return False
        
        return dfs(0)

