class Solution:
    def countDistinct(self, arr, k):
        from collections import defaultdict
        
        # Dictionary to store frequency of elements in the current window
        freq_map = defaultdict(int)
        distinct_count = []
        n = len(arr)
        
        # Initialize the first window
        for i in range(k):
            freq_map[arr[i]] += 1
        distinct_count.append(len(freq_map))
        
        # Slide the window
        for i in range(k, n):
            # Remove the element going out of the window
            freq_map[arr[i - k]] -= 1
            if freq_map[arr[i - k]] == 0:
                del freq_map[arr[i - k]]
            
            # Add the new element coming into the window
            freq_map[arr[i]] += 1
            
            # Append the count of distinct elements for this window
            distinct_count.append(len(freq_map))
        
        return distinct_count
