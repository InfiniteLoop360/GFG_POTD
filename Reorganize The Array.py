### Problem Understanding:
'''You are given an array `arr[]` of size `N`, where each element's value can either be equal to its index or not. Your task is to rearrange the elements of the array such that `arr[i] == i`. If an element `i` is not present in the array, then `arr[i] = -1`. The goal is to achieve this in O(N) time and O(1) extra space (in-place).

### Solution Approach:

We can solve this problem efficiently by using the following approach:

### Step-by-Step Approach:

#### 1. **Iterate Over Each Element of the Array**:
   - For each element `arr[i]`, the idea is to place it in its correct position, i.e., at index `arr[i] = i` (if `arr[i]` exists and is not `-1`).
   - If an element is already in its correct position or if it's `-1`, we skip to the next element.

#### 2. **Swapping Logic**:
   - When an element `arr[i]` is not `-1` and it is not in its correct position (i.e., `arr[i] != i`), we need to move it to its correct position.
   - Swap the current element `arr[i]` with the element at its correct index `arr[arr[i]]`. This ensures that element `arr[i]` goes to index `i`.
   - We repeat this process until the element `arr[i]` is either placed in its correct position or there is no valid element to swap (i.e., a `-1` is encountered).
   
   This ensures that each element `arr[i]` ends up in its correct position or the position is marked with `-1` if the element does not exist.

#### 3. **Mark Missing Elements as `-1`**:
   - Once the array is rearranged, a second pass is made to mark any index `i` where `arr[i] != i` as `-1`. This is done to ensure that positions where elements are missing are properly marked with `-1`.

#### 4. **Time Complexity**:
   - The process of rearranging the array is done in **O(N)** time. Each element is swapped at most once, so the overall number of operations is linear in the size of the array.
   - The second pass to mark the missing elements is also done in O(N), so the total time complexity is **O(N)**.

#### 5. **Space Complexity**:
   - Since we are rearranging the elements in place and are not using any extra data structures, the **space complexity** is **O(1)**.

---

### Detailed Example:

#### Input:
```
arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
```

#### Step-by-Step Execution:

1. **Initial Array**:
   ```
   arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
   ```

2. **First Pass (Swapping Elements)**:
   - **Index 0**: `arr[0] = -1`, no action needed.
   - **Index 1**: `arr[1] = -1`, no action needed.
   - **Index 2**: `arr[2] = 6`. Swap `arr[2]` with `arr[6]`:
     ```
     arr = [-1, -1, 2, 1, 9, 3, 6, -1, 4, -1]
     ```
     Now `arr[2] = 2`, which is correct.
   - **Index 3**: `arr[3] = 1`. Swap `arr[3]` with `arr[1]`:
     ```
     arr = [-1, 1, 2, -1, 9, 3, 6, -1, 4, -1]
     ```
     Now `arr[3] = -1`, which needs no further action.
   - **Index 4**: `arr[4] = 9`. Swap `arr[4]` with `arr[9]`:
     ```
     arr = [-1, 1, 2, -1, -1, 3, 6, -1, 4, 9]
     ```
     Now `arr[4] = -1`, which needs no further action.
   - **Index 5**: `arr[5] = 3`. Swap `arr[5]` with `arr[3]`:
     ```
     arr = [-1, 1, 2, 3, -1, -1, 6, -1, 4, 9]
     ```
     Now `arr[5] = -1`, which needs no further action.
   - **Index 6**: `arr[6] = 6`, which is correct.
   - **Index 7**: `arr[7] = -1`, no action needed.
   - **Index 8**: `arr[8] = 4`. Swap `arr[8]` with `arr[4]`:
     ```
     arr = [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]
     ```
     Now `arr[8] = -1`, which needs no further action.
   - **Index 9**: `arr[9] = 9`, which is correct.

3. **Second Pass (Marking Missing Elements)**:
   - After the first pass, we have:
     ```
     arr = [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]
     ```
   - Now, we make a second pass over the array and ensure that all indices where `arr[i] != i` are set to `-1`:
     - **Index 0**: `arr[0] != 0`, set `arr[0] = -1`.
     - **Index 5**: `arr[5] != 5`, set `arr[5] = -1`.
     - **Index 7**: `arr[7] != 7`, set `arr[7] = -1`.
     - **Index 8**: `arr[8] != 8`, set `arr[8] = -1`.

4. **Final Output**:
   ```
   arr = [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]
   ```

---

### Conclusion:

- The key idea is to place each element at its correct index if it exists in the array, and mark the missing elements with `-1`.
- By using in-place swaps and a second pass to mark missing elements, the solution is efficient with **O(N)** time complexity and **O(1)** auxiliary space.
'''

class Solution:
    def rearrange(self, arr):
        n = len(arr)

        # Swap elements to their correct positions while ignoring -1s
        for i in range(n):
            while arr[i] != -1 and arr[i] != i:
                arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
        
        # For elements that are not at their index, mark them as -1
        for i in range(n):
            if arr[i] != i:
                arr[i] = -1

        return arr
