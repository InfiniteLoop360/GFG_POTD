'''
Subarray range with given sum

Given an unsorted array of integers arr[], and a target tar, determine the number of subarrays whose elements sum up to the target value.

Examples:

Input: arr[] = [10, 2, -2, -20, 10] , tar = -10
Output: 3
Explanation: Subarrays with sum -10 are: [10, 2, -2, -20], [2, -2, -20, 10] and [-20, 10].
Input: arr[] = [1, 4, 20, 3, 10, 5] , tar = 33
Output: 1
Explanation: Subarray with sum 33 is: [20,3,10].
Expected Time Complexity: O(n)
Expected Auxilary Space: O(n)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
To solve this problem efficiently, we can use the concept of prefix sums and a hash map (dictionary) to store the frequency of each prefix sum encountered. This allows us to find subarrays with a target sum in \( O(n) \) time complexity.

### Approach:

1. **Prefix Sum**: The sum of elements from the start of the array up to the current index.
   - If the sum of elements between two indices \( i \) and \( j \) is equal to the target \( \text{tar} \), then:
     \[
     \text{sum}(i \, \text{to} \, j) = \text{prefix\_sum}(j) - \text{prefix\_sum}(i-1)
     \]
   - Rearranging, we get:
     \[
     \text{prefix\_sum}(i-1) = \text{prefix\_sum}(j) - \text{tar}
     \]
   - So, for each prefix sum, we look for the count of previous prefix sums that satisfy this condition.

2. **Hash Map**: We maintain a dictionary (hash map) to store the frequency of each prefix sum. The key will be the prefix sum, and the value will be how many times this sum has occurred.

### Steps:
1. Initialize a variable `current_sum` to keep track of the cumulative sum (prefix sum).
2. Use a dictionary `prefix_sum_count` to store the frequency of each prefix sum.
3. As you iterate through the array:
   - Update the `current_sum`.
   - Check if \( \text{current\_sum} - \text{tar} \) exists in the dictionary. If it does, it means there's a subarray that sums to the target.
   - Update the dictionary with the current prefix sum.
4. Count all subarrays that satisfy the condition.

'''
class Solution:
    # Complete this function
    # Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self, arr, tar):
        # Dictionary to store the prefix sums and their frequencies
        prefix_sum_count = {0: 1}
        current_sum = 0
        count = 0
        
        # Iterate over the array
        for num in arr:
            # Update the current prefix sum
            current_sum += num
            
            # Check if there's a prefix sum that gives the required sum
            if current_sum - tar in prefix_sum_count:
                count += prefix_sum_count[current_sum - tar]
            
            # Update the prefix sum count
            if current_sum in prefix_sum_count:
                prefix_sum_count[current_sum] += 1
            else:
                prefix_sum_count[current_sum] = 1
        
        return count

# Example usage:
arr = [10, 2, -2, -20, 10]
tar = -10
sol = Solution()
print(sol.subArraySum(arr, tar))  # Output: 3

'''

### Explanation:

1. **Dictionary `prefix_sum_count`**: This stores the frequency of each prefix sum encountered during the iteration. We initialize it with `{0: 1}` because a sum of 0 is trivially a valid prefix (helps in case a subarray from the beginning equals the target).
2. **Current Prefix Sum**: As we traverse the array, we calculate the cumulative sum (`current_sum`).
3. **Checking for Target**: For each new cumulative sum, we check if \( \text{current\_sum} - \text{tar} \) exists in the dictionary. If it does, it means a subarray that sums to `tar` exists.
4. **Updating the Dictionary**: After processing each element, we update the frequency of the `current_sum` in the dictionary.

### Time Complexity:
- **O(n)**: We are traversing the array once and performing constant time operations (dictionary lookup and update) for each element.

### Space Complexity:
- **O(n)**: In the worst case, we might store \( n \) different prefix sums in the dictionary.

### Example:

**Input**:
```python
arr = [10, 2, -2, -20, 10]
tar = -10
```

**Output**:
```python
3
```

**Explanation**:
The subarrays that sum to -10 are:
- `[10, 2, -2, -20]`
- `[2, -2, -20, 10]`
- `[-20, 10]`

Thus, the result is 3.
'''
