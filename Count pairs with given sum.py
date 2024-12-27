class Solution:
    # Complete the below function
    def countPairs(self, arr, target):
        # Dictionary to store frequency of elements
        freq = {}
        count = 0

        # Traverse the array
        for num in arr:
            # Calculate the complement
            complement = target - num

            # If complement exists in the dictionary, add its frequency to the count
            if complement in freq:
                count += freq[complement]

            # Update the frequency of the current number
            freq[num] = freq.get(num, 0) + 1

        return count
