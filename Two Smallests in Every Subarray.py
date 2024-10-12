'''
Two Smallests in Every Subarray
Given an array of integers arr, the task is to find and return the maximum sum of the smallest and second smallest element among all possible subarrays of size greater than one. If it is not possible, then return -1.

Examples:

Input: arr = [4, 3, 1, 5, 6]
Output: 11
Explanation: Subarrays with smallest and second smallest are,
Subarray: [4, 3], smallest = 3, second smallest = 4, sum = 7
Subarray: [4, 3, 1], smallest = 1, second smallest = 3, sum = 4
Subarray: [4, 3, 1, 5], smallest = 1, second smallest = 3, sum = 4
Subarray: [4, 3, 1, 5, 6], smallest = 1, second smallest = 3, sum = 4
Subarray: [3, 1], smallest = 1, second smallest = 3, sum = 4
Subarray: [3, 1, 5], smallest = 1, second smallest = 3, sum = 4
Subarray: [3, 1, 5, 6], smallest = 1, second smallest = 3, sum = 4
Subarray: [1, 5], smallest = 1, second smallest = 5, sum = 6
Subarray: [1, 5, 6] ,smallest = 1, second smallest = 5, sum = 6
Subarray: [5, 6], smallest = 5, second smallest = 6, sum = 11
Maximum sum among all above choices is, 5 + 6 = 11, hence the answer is 11.
Input: arr = [1]
Output: -1
Explanation: Here the size of array is 1, but we need minimum 2 elements. Hence, the answer is -1.
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
To solve this problem efficiently, we need to find subarrays of size 2 in the given array and compute the sum of the smallest and second smallest elements in each subarray. Since we are dealing with only subarrays of size 2, this can be done by simply comparing adjacent elements in the array.

The solution will involve the following steps:

1. Traverse the array and form subarrays of size 2 (adjacent pairs).
2. For each adjacent pair, compute the sum.
3. Keep track of the maximum sum encountered.
4. If the array has fewer than 2 elements, return `-1` since it's impossible to form any subarrays of size 2.

### Approach:
- Iterate through the array and calculate the sum of each adjacent pair.
- Return the maximum sum of these adjacent pairs.

### Time Complexity:
- We traverse the array once, so the time complexity is \(O(n)\).
- We don't use extra space except for a few variables, so the space complexity is \(O(1)\).

'''

class Solution:
    def pairWithMaxSum(self, arr):
        # If the array length is less than 2, return -1
        if len(arr) < 2:
            return -1
        
        # Initialize max_sum to a very small value
        max_sum = float('-inf')
        
        # Iterate through the array and find the sum of adjacent pairs
        for i in range(len(arr) - 1):
            current_sum = arr[i] + arr[i + 1]
            # Update max_sum if the current pair sum is greater
            max_sum = max(max_sum, current_sum)
        
        return max_sum
'''
### Explanation:
1. **Input Check**: We first check if the array has fewer than 2 elements. If so, we return `-1` since we need at least two elements to form a subarray.
2. **Iterating through the Array**: We loop through the array from index `0` to `len(arr) - 2`, forming pairs using `arr[i]` and `arr[i + 1]`. For each pair, we calculate their sum.
3. **Track Maximum Sum**: We keep track of the maximum sum encountered so far.
4. **Return Maximum Sum**: After the loop, we return the maximum sum of the adjacent pairs.

### Example:

#### Input 1:
```python
arr = [4, 3, 1, 5, 6]
solution = Solution()
print(solution.pairWithMaxSum(arr))
```
#### Output:
```
11
```

#### Input 2:
```python
arr = [1]
solution = Solution()
print(solution.pairWithMaxSum(arr))
```
#### Output:
```
-1
```

This solution efficiently handles the task in \(O(n)\) time, and it ensures minimal space usage, fulfilling the problem's constraints.
'''
