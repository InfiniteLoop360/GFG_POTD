class Solution:
    def binstr(self, n):
        result = []

        def backtrack(curr):
            # If length is n, store it
            if len(curr) == n:
                result.append(curr)
                return
            # Add '0' and recurse
            backtrack(curr + "0")
            # Add '1' and recurse
            backtrack(curr + "1")

        backtrack("")
        return result
