class Solution:
    def subarrayXor(self, arr, k):
        xor_map = {}
        xor_sum = 0
        count = 0
        
        for num in arr:
            # Update the cumulative XOR
            xor_sum ^= num
            
            # Check if the cumulative XOR matches k
            if xor_sum == k:
                count += 1
            
            # Check if there is a prefix with XOR = xor_sum ^ k
            if xor_sum ^ k in xor_map:
                count += xor_map[xor_sum ^ k]
            
            # Update the map with the current XOR
            xor_map[xor_sum] = xor_map.get(xor_sum, 0) + 1
        
        return count
