class Solution:
    def findMajority(self, arr):
        # Step 1: Initialize two candidates and their counts
        candidate1, candidate2, count1, count2 = None, None, 0, 0

        # Step 2: First pass to find the two potential majority elements
        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 3: Verify the two candidates
        count1, count2 = 0, 0
        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        # Step 4: Check if the candidates occur more than n/3 times
        result = []
        if count1 > len(arr) // 3:
            result.append(candidate1)
        if count2 > len(arr) // 3:
            result.append(candidate2)

        # Step 5: Return the result in sorted order
        return sorted(result)
