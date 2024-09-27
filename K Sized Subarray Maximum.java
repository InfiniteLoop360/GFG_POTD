/*Approach:
1. Use a deque: The idea is to maintain a sliding window of size k and keep track of the indices of the array elements in the deque.
2. Maintain deque properties: 
      Elements in the deque are in decreasing order. So the front of the deque will always contain the index of the maximum element of the current window.
      Remove elements from the deque that are no longer in the current window.
      For each new element, remove all elements in the deque that are smaller than the current element (as they can't be the maximum for any upcoming window).
3. Sliding the window: As we slide the window from left to right, we maintain the deque so that the front of the deque always has the maximum element's index for the current window.
4. Return result: At each step, add the element at the front of the deque to the result list as the maximum for that window.*/


class Solution {
    // Function to find maximum of each subarray of size k.
    public ArrayList<Integer> max_of_subarrays(int k, int arr[]) {
        ArrayList<Integer> result = new ArrayList<>(); // To store the result
        Deque<Integer> deque = new LinkedList<>(); // To store the indices of useful elements

        // Traverse the array
        for (int i = 0; i < arr.length; i++) {
            // Remove elements from the front of the deque that are outside the current window
            if (!deque.isEmpty() && deque.peek() == i - k) {
                deque.poll();
            }

            // Remove elements from the back of the deque that are smaller than the current element
            while (!deque.isEmpty() && arr[deque.peekLast()] <= arr[i]) {
                deque.pollLast();
            }

            // Add the current element index to the back of the deque
            deque.offer(i);

            // Once we have a window of size k, the largest element is at the front of the deque
            if (i >= k - 1) {
                result.add(arr[deque.peek()]);
            }
        }

        return result;
    }
}
