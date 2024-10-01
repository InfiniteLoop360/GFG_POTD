'''
Solution approach:

1. **Convert Linked Lists to Numbers**:
   - The key idea is to treat each linked list as representing a number, where each node in the list contributes one digit to the number.
   - Start from the head of the list and traverse towards the end, constructing the number by treating the nodes as digits in a base-10 number.
   - For example, a linked list `3 -> 2 -> 1` represents the number 321.

2. **Multiplication of Two Numbers**:
   - Once you have converted both linked lists into numbers, simply multiply them together.
   - Since the result could be large, take the modulo \(10^9 + 7\) after multiplying the two numbers.

3. **Steps**:
   - **Step 1**: Traverse the first linked list and build the first number.
   - **Step 2**: Traverse the second linked list and build the second number.
   - **Step 3**: Multiply the two numbers.
   - **Step 4**: Return the result modulo \(10^9 + 7\).

4. **Optimization Considerations**:
   - **Modulo Operation**: At every step of constructing the number, perform the modulo operation to avoid overflow.
   - **Time Complexity**: The time complexity is \(O(n + m)\), where \(n\) is the number of nodes in the first linked list and \(m\) is the number of nodes in the second linked list.

### Detailed Steps:

1. **Traversing Linked List**:
   - Initialize a variable (say `num`) as 0.
   - Traverse each node of the linked list and append the current node’s value to the number.
   - Multiply the existing number by 10 and add the current node's data (which is the digit).
   - Keep updating the number by taking modulo \(10^9 + 7\) at each step to avoid large numbers.

2. **Multiply Numbers**:
   - Once you have the integer representation of both linked lists, multiply them.
   - Take the final result modulo \(10^9 + 7\).

### Example Walkthrough:

**Example 1**:
- Input:
  - L1: `3 -> 2` (which represents 32)
  - L2: `2` (which represents 2)
- Process:
  - First number from L1 = 32
  - Second number from L2 = 2
  - Multiplying these: 32 * 2 = 64
- Output:
  - 64

**Example 2**:
- Input:
  - L1: `1 -> 0 -> 0` (which represents 100)
  - L2: `1 -> 0` (which represents 10)
- Process:
  - First number from L1 = 100
  - Second number from L2 = 10
  - Multiplying these: 100 * 10 = 1000
- Output:
  - 1000
'''

class Solution:
    MOD = 10**9 + 7
    
    def get_number_from_list(self, head):
        num = 0
        while head:
            num = (num * 10 + head.data) % self.MOD
            head = head.next
        return num

    def multiply_two_lists(self, first, second):
        # Step 1: Get the integer values from both linked lists
        num1 = self.get_number_from_list(first)
        num2 = self.get_number_from_list(second)
        
        # Step 2: Multiply the numbers and return result modulo 10^9 + 7
        result = (num1 * num2) % self.MOD
        
        return result
