
/*Problem: 
Minimal Cost
There is an array arr of heights of stone and Geek is standing at the first stone and can jump to one of the following: Stone i+1, i+2, ... i+k stone, where k is the maximum number of steps that can be jumped and cost will be |hi-hj| is incurred, where j is the stone to land on. Find the minimum possible total cost incurred before the Geek reaches the last stone.

Example:
Input: k = 3, arr[]= [10, 30, 40, 50, 20]
Output: 30
Explanation: Geek will follow the path 1->2->5, the total cost would be | 10-30| + |30-20| = 30, which is minimum
Input: k = 1, arr[]= [10, 20, 10]
Output: 20
Explanation: Geek will follow the path 1->2->3, the total cost would be |10 - 20| + |20 - 10| = 20.
Expected Time Complexity: O(n*k)
Expected Auxilary Space: O(n)

Solution approach:
Key Points:
#Dynamic Programming (dp[]) is used to store the minimum cost to reach each stone.
#For each stone i, the minimum cost is calculated by checking jumps from up to k previous stones.
#Time Complexity: O(n * k) due to the nested loop.
#Space Complexity: O(n) for the dp array.
*/
  
class Solution {
    public int minimizeCost(int k, int[] arr) {
        int n = arr.length;
        int[] dp = new int[n];
        
        // Initialize dp array with a large number (since we are looking for minimum)
        for (int i = 1; i < n; i++) {
            dp[i] = Integer.MAX_VALUE;
        }
        
        // The cost to stay at the first stone is 0
        dp[0] = 0;
        
        // Iterate over each stone
        for (int i = 1; i < n; i++) {
            // Check all stones that can be reached from the current stone i
            for (int j = 1; j <= k && i - j >= 0; j++) {
                dp[i] = Math.min(dp[i], dp[i - j] + Math.abs(arr[i] - arr[i - j]));
            }
        }
        
        // The minimum cost to reach the last stone will be stored in dp[n-1]
        return dp[n - 1];
    }
}
