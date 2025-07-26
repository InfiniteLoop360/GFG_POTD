class Solution:
    def findMajority(self, arr):
        n = len(arr)
        if not arr:
            return []
        
        # Step 1: Find potential candidates
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
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
        
        # Step 2: Verify the candidates
        result = []
        if arr.count(candidate1) > n // 3:
            result.append(candidate1)
        if candidate2 != candidate1 and arr.count(candidate2) > n // 3:
            result.append(candidate2)

        return sorted(result)
