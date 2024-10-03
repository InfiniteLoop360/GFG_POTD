'''
Majority Vote
You are given an array of integer nums[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return -1. 

Note: The answer should be returned in an incresing format.

Examples:

Input: nums = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
Output: [5, 6]
Explanation: 5 and 6 occur more n/3 times.

Input: nums = [1, 2, 3, 4, 5]
Output: [-1]
Explanation: no candidate occur more than n/3 times.

Expected Time Complexity: O(n)
Expected Space Complexity: O(1)
--------------------------------------------

Approach:
The problem asks to find all the candidates that appear more than `n/3` times in an array, where `n` is the total number of elements. This can be solved using an optimized version of the Boyer-Moore Voting Algorithm, which works for finding elements that appear more than `n/3` times.

Steps:
1. **Two Candidates Voting System**:
   - We keep track of two potential candidates and their corresponding vote counts.
   - We traverse the array, adjusting the candidate counts based on matching or non-matching numbers.
   
2. **Verify the Two Candidates**:
   - Once potential candidates are identified, iterate through the array one more time to verify if these candidates appear more than `n/3` times.

3. **Return Results**:
   - If no candidates satisfy the condition, return `[-1]`. Otherwise, return the valid candidates in increasing order.
'''
  
class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, nums):
        if not nums:
            return [-1]
        
        # Step 1: Find potential candidates using Boyer-Moore Voting Algorithm
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Verify if the candidates occur more than n/3 times
        count1, count2 = 0, 0
        n = len(nums)
        
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        # Step 3: Prepare the result
        result = []
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)

        # Step 4: Return result in increasing order or [-1] if no majority
        return sorted(result) if result else [-1]

# Example usage
sol = Solution()
print(sol.findMajority([2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]))  # Output: [5, 6]
print(sol.findMajority([1, 2, 3, 4, 5]))  # Output: [-1]


'''
### Explanation:
1. **Boyer-Moore Voting Algorithm**:
   - We keep track of two candidates and two vote counts.
   - In each iteration:
     - If the current number matches either of the candidates, increment their count.
     - If either count becomes 0, we reset the candidate to the current number.
     - If the number doesn’t match either candidate and both candidates have non-zero counts, decrement both counts.

2. **Final Check**:
   - After identifying potential candidates, we count how many times they actually appear in the array.
   - Only candidates with occurrences greater than `n/3` are added to the result.

3. **Time Complexity**:
   - **O(n)**: We traverse the array twice — once to find potential candidates and once to verify them.
   
4. **Space Complexity**:
   - **O(1)**: Only a constant amount of extra space is used for storing candidates and counts. The final result doesn’t count towards space complexity as it depends on the number of output candidates.

'''
