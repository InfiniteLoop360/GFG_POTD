class Solution {
  public:
    int rotateDelete(vector<int> &arr) {
        // Initial value of k (starts from 1)
        int k = 1;
        
        // Continue until there is only one element left in the vector
        while (arr.size() > 1) {
            // Rotate the array: Move the last element to the front
            int lastElement = arr.back();
            arr.pop_back();
            arr.insert(arr.begin(), lastElement);

            // Determine the index to be deleted (k-th from the last)
            int deleteIndex = arr.size() - k;

            // Delete the k-th element from the last if the index is valid
            if (deleteIndex >= 0) {
                arr.erase(arr.begin() + deleteIndex);
            } else {
                arr.erase(arr.begin()); // If index goes out of bounds, remove the first element
            }

            // Increment k for the next operation
            k++;
        }

        // Return the last remaining element
        return arr[0];
    }
};
