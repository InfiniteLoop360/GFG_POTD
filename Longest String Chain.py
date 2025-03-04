class Solution:
    def longestStringChain(self, words):
        words.sort(key=len)  # Sort words by length
        dp = {}  # Dictionary to store the longest chain ending at each word
        max_chain = 1  # At least one word can always form a chain

        for word in words:
            dp[word] = 1  # Minimum chain length for any word is 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]  # Remove one character
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)  # Update max chain length
            max_chain = max(max_chain, dp[word])  # Update overall longest chain

        return max_chain
