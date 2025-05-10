    def longestSubarray(self, arr, k):
        prefix_sum = 0
        max_length = 0
        prefix_map = {0: -1}
        
        for i in range(len(arr)):
            if arr[i] > k:
                prefix_sum += 1
            else:
                prefix_sum -= 1
                
            if prefix_sum > 0:
                max_length = i + 1
                
            if prefix_sum - 1 in prefix_map:
                max_length = max(max_length, i - prefix_map[prefix_sum - 1])
                
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i
                
        return max_length
