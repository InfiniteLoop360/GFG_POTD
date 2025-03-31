class Solution:
    def maxPartitions(self, s):
        last_occurrence = {char: i for i, char in enumerate(s)}  # Step 1: Store last occurrence of each char
        partitions = 0
        end = 0
        start = 0
        
        for i, char in enumerate(s):  
            end = max(end, last_occurrence[char])  # Extend the partition boundary
            
            if i == end:  # Found a valid partition
                partitions += 1
                start = i + 1  # Move start to the next partition
        
        return partitions
