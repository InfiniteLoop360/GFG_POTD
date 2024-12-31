class Solution:
    # Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self, arr):
        # Using a set to store all unique elements
        num_set = set(arr)
        max_length = 0
        
        # Iterating through each element in the set
        for num in num_set:
            # Check if it's the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                # Count the length of the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                # Update the maximum length
                max_length = max(max_length, current_length)
        
        return max_length
