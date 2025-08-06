class Solution:
    def romanToDecimal(self, s):
        # Mapping of Roman numerals to integers
        val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        n = len(s)
        if n == 0:
            return 0
        
        total = 0
        i = 0
        
        while i < n:
            # If this symbol has a smaller value than the next symbol, subtract it
            if i + 1 < n and val[s[i]] < val[s[i + 1]]:
                total -= val[s[i]]
            else:
                total += val[s[i]]
            i += 1
        
        return total
