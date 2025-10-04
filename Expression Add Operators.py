class Solution:
    def findExpr(self, s, target):
        res = []
        
        def backtrack(index, path, calc, tail):
            # Base case: reached end of string
            if index == len(s):
                if calc == target:
                    res.append(path)
                return
            
            # Try all possible splits
            for i in range(index, len(s)):
                # Avoid numbers with leading zeros
                if i > index and s[index] == '0':
                    break
                    
                curStr = s[index:i+1]
                curNum = int(curStr)
                
                if index == 0:
                    # First number, just start path
                    backtrack(i+1, curStr, curNum, curNum)
                else:
                    # Try +
                    backtrack(i+1, path + "+" + curStr, calc + curNum, curNum)
                    # Try -
                    backtrack(i+1, path + "-" + curStr, calc - curNum, -curNum)
                    # Try *
                    backtrack(i+1, path + "*" + curStr, calc - tail + tail * curNum, tail * curNum)
        
        backtrack(0, "", 0, 0)
        return sorted(res)  # Driver requires lexicographic order
