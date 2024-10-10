'''
Max distance between same elements

Given an array arr[] with repeated elements, the task is to find the maximum distance between two occurrences of an element.

Note: You may assume that every input array has repetitions.

Examples:

Input: arr = [1, 1, 2, 2, 2, 1]
Output: 5
Explanation: distance for 1 is: 5-0 = 5, distance for 2 is : 4-2 = 2, So max distance is 5.
Input: arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
Output: 10
Explanation: maximum distance for 2 is 11-1 = 10, maximum distance for 1 is 4-2 = 2 ,maximum distance for 4 is 10-5 = 5, So max distance is 10.
Expected Time Complexity :  O(n)
Expected Auxilliary Space : O(n)
------------------------------------------------------------------------------------------------------------------------------------------------------------
To solve this problem efficiently in \( O(n) \) time complexity, we can keep track of the first occurrence of each element in a dictionary as we iterate through the array. For every subsequent occurrence of the element, we compute the distance from its first occurrence, and we keep updating the maximum distance encountered.

### Approach:

1. **Initialize a dictionary** to store the first occurrence index of each element.
2. As we traverse the array, for each element:
   - If the element is **encountered for the first time**, store its index in the dictionary.
   - If the element has been encountered before, calculate the distance from its first occurrence and update the maximum distance if necessary.
3. Finally, return the maximum distance found.

'''

class Solution:
    # Function to return the maximum distance between two occurrences of an element.
    def maxDistance(self, arr):
        # Dictionary to store the first occurrence index of each element.
        first_occurrence = {}
        max_dist = 0
        
        # Traverse the array
        for i in range(len(arr)):
            if arr[i] not in first_occurrence:
                # Store the first occurrence index of the element
                first_occurrence[arr[i]] = i
            else:
                # Calculate the distance from the first occurrence
                distance = i - first_occurrence[arr[i]]
                # Update the maximum distance
                max_dist = max(max_dist, distance)
        
        return max_dist
'''

### Explanation:

- We use a dictionary `first_occurrence` to keep track of the index where each element is first seen.
- For every subsequent occurrence of the same element, we compute the distance from the first occurrence and update the `max_dist` if the distance is larger than the current `max_dist`.

### Time and Space Complexity:

- **Time Complexity**: \( O(n) \) where \( n \) is the length of the array, as we are traversing the array only once.
- **Space Complexity**: \( O(n) \) due to the space required for storing the first occurrences of elements in the dictionary.

### Example:

'''
arr1 = [1, 1, 2, 2, 2, 1]
arr2 = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]

sol = Solution()
print(sol.maxDistance(arr1))  # Output: 5
print(sol.maxDistance(arr2))  # Output: 10

'''
This solution works efficiently and returns the correct maximum distance for the given examples.
'''
