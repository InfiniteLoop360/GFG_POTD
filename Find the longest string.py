class Solution():
    def longestString(self, arr):
        word_set = set(arr)
        longest = ""

        for word in arr:
            valid = True
            for i in range(1, len(word)):
                if word[:i] not in word_set:
                    valid = False
                    break
            if valid:
                if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                    longest = word
                    
        return longest
