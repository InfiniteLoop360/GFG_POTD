class Solution {
    // Function to merge the arrays.
    public void mergeArrays(int a[], int b[]) {
        int n = a.length;
        int m = b.length;

        // Start from the end of the first array and the start of the second array
        int i = n - 1;
        int j = 0;

        // Swap elements if they are out of order
        while (i >= 0 && j < m) {
            if (a[i] > b[j]) {
                // Swap the elements
                int temp = a[i];
                a[i] = b[j];
                b[j] = temp;
            }
            i--;
            j++;
        }

        // Sort both arrays to finalize the merge
        Arrays.sort(a);
        Arrays.sort(b);
    }
}
