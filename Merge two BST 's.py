'''Solution Approach:

1. In-order Traversal: Since an in-order traversal of a BST gives the elements in sorted order, we perform an in-order traversal on both trees to collect their elements into two sorted lists, list1 and list2.
2. Merge Two Sorted Lists: We then merge these two sorted lists using a two-pointer approach to create the final sorted merged list.
3. Time Complexity: 
   In-order traversal takes O(m) and O(n) time for BST1 and BST2, respectively.
   Merging two sorted lists takes O(m + n) time.
   Hence, the overall time complexity is O(m + n).
4. Auxiliary Space: 
   We are using space to store the in-order traversal results and the merged list, which takes O(m + n) space.
   Additionally, we use space for recursion, which depends on the height of the trees (logarithmic in the best case, but linear in the worst case).

Example:
For the input BST1 and BST2:

BST1:
       5
     /   \
    3     6
   / \
  2   4
BST2:
        2
      /   \
     1     3
            \
             7
            /
           6
The output will be:
[1, 2, 2, 3, 3, 4, 5, 6, 6, 7]
'''

class Solution:
    def inorderTraversal(self, root, res):
        # Helper function to perform in-order traversal
        if root:
            self.inorderTraversal(root.left, res)
            res.append(root.data)
            self.inorderTraversal(root.right, res)
    
    def mergeSortedArrays(self, list1, list2):
        # Merging two sorted lists
        i, j = 0, 0
        merged_list = []
        
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                merged_list.append(list1[i])
                i += 1
            else:
                merged_list.append(list2[j])
                j += 1
                
        # Append remaining elements of list1 if any
        while i < len(list1):
            merged_list.append(list1[i])
            i += 1
        
        # Append remaining elements of list2 if any
        while j < len(list2):
            merged_list.append(list2[j])
            j += 1
            
        return merged_list
    
    def merge(self, root1, root2):
        # Step 1: Perform in-order traversal of both BSTs
        list1, list2 = [], []
        self.inorderTraversal(root1, list1)
        self.inorderTraversal(root2, list2)
        
        # Step 2: Merge the two sorted lists
        return self.mergeSortedArrays(list1, list2)
