class Solution:
    def multiplyStrings(self, s1, s2):
        # Remove leading zeros
        s1 = s1.lstrip('0')
        s2 = s2.lstrip('0')
        
        if not s1 or not s2:
            return "0"
        
        # Check if result should be negative
        negative = False
        if s1[0] == '-':
            negative = not negative
            s1 = s1[1:]
        if s2[0] == '-':
            negative = not negative
            s2 = s2[1:]
        
        n, m = len(s1), len(s2)
        result = [0] * (n + m)
        
        # Start multiplying from the last digits
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                mult = (ord(s1[i]) - ord('0')) * (ord(s2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1
                sum = mult + result[p2]
                
                result[p2] = sum % 10
                result[p1] += sum // 10
        
        # Skip leading zeros
        res = []
        for num in result:
            if not (len(res) == 0 and num == 0):
                res.append(str(num))
        
        if not res:
            return "0"
        
        final_result = ''.join(res)
        if negative:
            final_result = '-' + final_result
        
        return final_result
