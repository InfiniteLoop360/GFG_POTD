/*
### Problem Statement 

Nearest multiple of 10

A string str is given to represent a positive number. The task is to round str to the nearest multiple of 10.  If you have two multiples equally apart from str, choose the smallest element among them.

Examples:

Input: str = 29 
Output: 30
Explanation: Close multiples are 20 and 30, and 30 is the nearest to 29. 
Input: str = 15
Output: 10
Explanation: 10 and 20 are equally distant multiples from 20. The smallest of the two is 10.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### Solution Approach

1. **Check the Last Digit**: 
   - The last character of the string is examined to determine how to round the number.
   - If this character (last digit) is less than or equal to '5', it is changed to '0', effectively rounding down to the nearest lower multiple of 10.
   - If it is greater than '5', the last digit is again changed to '0', and the program then must consider how to handle the carry-over that might happen when we increment the next digit.

2. **Handle Carry-over**:
   - After setting the last digit to '0', we move to the second last digit (i.e., `n-2`) and check for '9's. If we encounter '9', we set it to '0' and continue moving left.
   - If we move past the first character and all characters have been turned into '0's (e.g., from '999' to '000'), we need to prepend '1' to the result to signify that we have rounded up to '1000'.
   - If we find a digit that is not '9', we simply increment that digit by 1 to complete the rounding up.

*/
class Solution {
  public:
    string roundToNearest(string str) {
        // Length of the string
        int n = str.length();
        
        // Check the last character of the string
        if (str[n-1] <= '5') {
            // Round down by setting last character to '0'
            str[n-1] = '0';
            return str; // Return the rounded down string
        }
        
        // Round up by setting last character to '0'
        str[n-1] = '0';
        int i = n - 2;
        
        // Handle carry-over for rounding up
        while (i >= 0 && str[i] == '9') {
            str[i] = '0'; // Set '9' to '0' and continue left
            i--;
        }
        
        // If we have gone past the first digit (i < 0), prepend '1'
        if (i < 0) {
            return '1' + str; // Example: '999' becomes '1000'
        } else {
            str[i]++; // Increment the first non-'9' digit by 1
        }
        
        return str; // Return the final rounded string
    }
};
/*

### Step-by-Step Execution

1. **Input**: For example, if `str` is `"29"`:
   - Length `n` is `2`.
   - Last character is `9` (greater than 5), so set `str[n-1]` to '0'.
   - The string becomes `"20"`.
   - Check the character before last (at index `0`), which is `2` (not '9'), so increment it to `3`.
   - Return the final string `"30"`.

2. **Input**: If `str` is `"999"`:
   - Length `n` is `3`.
   - Last character is `9` (greater than 5), so set `str[n-1]` to '0'.
   - The string becomes `"990"`.
   - Move to the second last character (at index `1`), which is also `9`, set it to '0'.
   - Move to the first character (at index `0`), which is `9`, set it to '0'.
   - Now `i` becomes `-1`, meaning we've processed all characters, so prepend '1'.
   - The final string becomes `"1000"`.

### Summary of  Approach

- This solution effectively handles rounding based on the last digit and considers potential carry-over when incrementing digits.
- It avoids unnecessary conversions between data types, keeping the operations efficient and straightforward for a string representation of a number.
- The overall time complexity of the solution is \(O(n)\), where \(n\) is the length of the input string, and the space complexity is \(O(1)\) since we modify the string in place. 

This approach is efficient and correctly adheres to the problem requirements, ensuring accurate rounding behavior.
  */
