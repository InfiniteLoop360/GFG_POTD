class Solution {
public:
    // Helper function to perform DFS and calculate the sum
    int dfs(Node* node, int currentNumber) {
        if (node == nullptr) {
            return 0;
        }
        
        // Update the current number formed
        currentNumber = currentNumber * 10 + node->data;

        // If it's a leaf node, return the current number
        if (node->left == nullptr && node->right == nullptr) {
            return currentNumber;
        }

        // Recursively call for left and right children
        int leftSum = dfs(node->left, currentNumber);
        int rightSum = dfs(node->right, currentNumber);

        // Return the total sum from both subtrees
        return leftSum + rightSum;
    }

    // Main function to calculate the total sum of all root-to-leaf paths
    int treePathsSum(Node* root) {
        return dfs(root, 0); // Start DFS from the root with an initial number of 0
    }
};
