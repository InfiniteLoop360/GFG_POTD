'''
Largest Pair Sum
Find the largest pair sum in an array of distinct integers.

Examples :

Input: arr[] = [12, 34, 10, 6, 40]
Output: 74
Explanation: Sum of 34 and 40 is the largest, i.e, 34 + 40 = 74.
Input: arr[] = [10, 20, 30]
Output: 50
Explanation: 20 + 30 = 50.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
To solve this problem efficiently with a time complexity of \(O(n)\) and auxiliary space of \(O(1)\), we need to find the two largest integers in the array and return their sum. Here’s a step-by-step breakdown:

1. **Initialization**: Start by initializing two variables (`first_max` and `second_max`) to the smallest possible integer values.
2. **Traverse the array**: Iterate over each element in the array:
   - If the current element is greater than `first_max`, update `second_max` to be `first_max` and `first_max` to be the current element.
   - Otherwise, if the current element is greater than `second_max` but less than or equal to `first_max`, update `second_max`.
3. **Return the sum** of the two largest elements (`first_max + second_max`).

'''
from typing import List

class Solution:
    def pairsum(self, arr: List[int]) -> int:
        # Initialize the two largest variables to a very small value
        first_max = second_max = float('-inf')
        
        # Traverse the array
        for num in arr:
            if num > first_max:
                second_max = first_max
                first_max = num
            elif num > second_max:
                second_max = num
        
        # Return the sum of the two largest numbers
        return first_max + second_max

# Example usage:
sol = Solution()
print(sol.pairsum([12, 34, 10, 6, 40]))  # Output: 74
print(sol.pairsum([10, 20, 30]))         # Output: 50

'''

### Explanation:
1. **Input**: The array `arr[] = [12, 34, 10, 6, 40]`
   - First iteration: `first_max = 12`, `second_max = -inf`
   - Second iteration: `first_max = 34`, `second_max = 12`
   - Third iteration: `first_max = 34`, `second_max = 12`
   - Fourth iteration: `first_max = 34`, `second_max = 12`
   - Fifth iteration: `first_max = 40`, `second_max = 34`
   
2. **Output**: The sum of the two largest integers, `40 + 34 = 74`.

This solution runs in \(O(n)\) time and uses constant space \(O(1)\).
'''
