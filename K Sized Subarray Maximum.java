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
