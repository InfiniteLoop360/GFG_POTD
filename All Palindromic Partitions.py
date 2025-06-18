class Solution:
    def palinParts(self, s):
        res = []
        path = []

        def isPalindrome(sub):
            return sub == sub[::-1]

        def backtrack(start):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                substr = s[start:end]
                if isPalindrome(substr):
                    path.append(substr)
                    backtrack(end)
                    path.pop()

        backtrack(0)
        return res
