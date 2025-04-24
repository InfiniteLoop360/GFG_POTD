class Solution:
    def getSingle(self, arr):
        result = 0
        for i in range(32):
            bit_count = sum((num >> i) & 1 for num in arr)
            if bit_count % 3:
                result |= (1 << i)
        # Convert to signed 32-bit int
        if result >= 2**31:
            result -= 2**32
        return result
