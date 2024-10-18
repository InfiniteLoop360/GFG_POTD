'''
To solve the problem of finding the element that appears an odd number of times in an array where every other element appears an even number of times, we can use the **XOR** operator.

### Key Concept:
- XOR has the following properties:
  1. \(a \oplus a = 0\) (XOR of a number with itself is 0).
  2. \(a \oplus 0 = a\) (XOR of a number with 0 is the number itself).
  3. XOR is commutative and associative.

Thus, when XORing all elements of the array together, elements that appear an even number of times will cancel out, leaving the number that appears an odd number of times.

### Approach:
1. Initialize a variable `result` to 0.
2. Traverse the array and XOR each element with `result`.
3. After the traversal, `result` will contain the number that appears an odd number of times.

'''
class Solution:
    
    def getSingle(self, arr):
        # Initialize result to 0
        result = 0
        
        # XOR all elements
        for num in arr:
            result ^= num
            
        # The result will hold the element that appears an odd number of times
        return result
'''

### Explanation:
- **Initialization**: We initialize `result` to 0.
- **XOR Loop**: As we iterate through the array, we XOR each number with `result`. Since XORing two equal numbers cancels them out (i.e., produces 0), only the number that appears an odd number of times will remain in `result`.
- **Return Value**: At the end of the loop, `result` contains the number that appears an odd number of times.

### Example Walkthrough:

1. **Input**: `arr = [1, 1, 2, 2, 2]`
   - Step-by-step XOR:
     - `result = 0`
     - `result ^= 1` → `result = 1`
     - `result ^= 1` → `result = 0` (since 1 XOR 1 = 0)
     - `result ^= 2` → `result = 2`
     - `result ^= 2` → `result = 0` (since 2 XOR 2 = 0)
     - `result ^= 2` → `result = 2`
   - **Output**: `2` (appears 3 times, which is odd)

2. **Input**: `arr = [8, 8, 7, 7, 6, 6, 1]`
   - Step-by-step XOR:
     - `result = 0`
     - `result ^= 8` → `result = 8`
     - `result ^= 8` → `result = 0`
     - `result ^= 7` → `result = 7`
     - `result ^= 7` → `result = 0`
     - `result ^= 6` → `result = 6`
     - `result ^= 6` → `result = 0`
     - `result ^= 1` → `result = 1`
   - **Output**: `1` (appears once, which is odd)

### Time Complexity:
- The time complexity is **O(n)**, where `n` is the number of elements in the array, as we are traversing the array once.

### Space Complexity:
- The space complexity is **O(1)** since we are using a constant amount of extra space (`result`).

This solution efficiently finds the element that appears an odd number of times in linear time and constant space.
'''
