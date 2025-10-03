class Solution:
    def possibleWords(self, arr):
        # Mapping of digits to letters
        mapping = {
            2: "abc", 3: "def", 4: "ghi", 5: "jkl",
            6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"
        }
        
        result = []
        
        def backtrack(index, path):
            # Base case: if we've formed a word of length = arr size
            if index == len(arr):
                result.append("".join(path))
                return
            
            digit = arr[index]
            
            # Skip if digit is 0 or 1
            if digit not in mapping:
                backtrack(index + 1, path)
                return
            
            # Explore all possible characters for this digit
            for char in mapping[digit]:
                path.append(char)      # Choose
                backtrack(index + 1, path)  # Explore
                path.pop()             # Undo choice (Backtrack)
        
        backtrack(0, [])
        return result
