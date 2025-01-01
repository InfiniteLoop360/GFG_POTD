class Solution:
    def anagrams(self, arr):
        # Dictionary to group words by their sorted form
        grouped_anagrams = {}
        
        for word in arr:
            # Sort the word to find its 'signature'
            signature = ''.join(sorted(word))
            
            # Add the word to its corresponding group
            if signature not in grouped_anagrams:
                grouped_anagrams[signature] = []
            grouped_anagrams[signature].append(word)
        
        # Return the grouped anagrams as a list
        return list(grouped_anagrams.values())
