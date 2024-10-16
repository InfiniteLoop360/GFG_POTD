'''
Two Swaps

Given a permutation of some of the first natural numbers in an array arr[], determine if the array can be sorted in exactly two swaps. A swap can involve the same pair of indices twice.

Return true if it is possible to sort the array with exactly two swaps, otherwise return false.

Examples:

Input: arr = [4, 3, 2, 1]
Output: true
Explanation: First, swap arr[0] and arr[3]. The array becomes [1, 3, 2, 4]. Then, swap arr[1] and arr[2]. The array becomes [1, 2, 3, 4], which is sorted.
Input: arr = [4, 3, 1, 2]
Output: false
Explanation: It is not possible to sort the array with exactly two swaps.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
To solve the problem of determining whether an array can be sorted using exactly two swaps, we need to evaluate the positions of the elements that are out of place. Here's how we can approach the solution:

### Approach:
1. **Identify Misplaced Elements**: First, we can compare the given array with its sorted version and identify the indices where the elements are different from what they should be in the sorted array.

2. **Count Misplaced Pairs**: We need to see how many positions are "misplaced." If there are exactly **two pairs of misplaced elements**, then it’s possible to sort the array using exactly two swaps.

3. **Swap Validity**: 
   - If we find exactly two pairs of indices that are out of place, we can swap them and check if the array becomes sorted after these two swaps.
   - If more than two elements are misplaced, or the swaps don't resolve the sorting issue, we return `False`.

'''
class Solution:
    def checkSorted(self, arr):
        # Create a sorted version of the array
        sorted_arr = sorted(arr)
        
        # Store indices where the elements differ from the sorted array
        mismatched_indices = []
        
        for i in range(len(arr)):
            if arr[i] != sorted_arr[i]:
                mismatched_indices.append(i)
        
        # If no mismatches, the array is already sorted
        if len(mismatched_indices) == 0:
            return True
        
        # If exactly 4 mismatches, we can potentially sort it with 2 swaps
        if len(mismatched_indices) == 4:
            i1, i2, i3, i4 = mismatched_indices
            
            # Check if swapping arr[i1] with arr[i4] and arr[i2] with arr[i3] sorts the array
            arr[i1], arr[i4] = arr[i4], arr[i1]  # First swap
            arr[i2], arr[i3] = arr[i3], arr[i2]  # Second swap
            
            if arr == sorted_arr:
                return True
            
        # Otherwise, it's not possible to sort the array with exactly two swaps
        return False

# Example usage:
sol = Solution()
print(sol.checkSorted([4, 3, 2, 1]))  # Output: True
print(sol.checkSorted([4, 3, 1, 2]))  # Output: False
'''

### Explanation of the Code:
1. **Sorting the Array**: We first generate a sorted version of the input array `sorted_arr`.
   
2. **Finding Mismatches**: We compare the original array `arr` with `sorted_arr` to find positions where the elements are different. These positions are stored in `mismatched_indices`.

3. **Condition for Sorting with Two Swaps**:
   - If there are **exactly 4 mismatches**, we perform two swaps: one between the first and last mismatched indices and another between the second and third mismatched indices.
   - After the swaps, we check if the array becomes sorted. If it does, we return `True`.

4. **Return False**: If the array cannot be sorted with exactly two swaps or there are more or fewer mismatched indices, we return `False`.

### Time Complexity:
- Sorting the array takes **O(n log n)**, and comparing the original and sorted arrays takes **O(n)**. Thus, the overall time complexity is **O(n log n)**, which is efficient for the given problem.

### Example Walkthrough:
1. **Input**: `[4, 3, 2, 1]`
   - Sorted version: `[1, 2, 3, 4]`
   - Mismatched indices: `[0, 1, 2, 3]`
   - First swap: Swap index `0` and `3` -> `[1, 3, 2, 4]`
   - Second swap: Swap index `1` and `2` -> `[1, 2, 3, 4]`
   - The array is now sorted, so the output is `True`.

2. **Input**: `[4, 3, 1, 2]`
   - Sorted version: `[1, 2, 3, 4]`
   - Mismatched indices: `[0, 1, 2, 3]`
   - After two swaps, the array is still not sorted, so the output is `False`.
'''
