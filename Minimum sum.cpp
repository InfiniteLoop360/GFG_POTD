class Solution {
  public:
    string minSum(vector<int> &arr) {
        // code here
        sort(arr.begin(), arr.end());
        string sb1, sb2, ans;
        bool flag = true;
        
        // Split digits alternately between sb1 and sb2
        for (int i : arr) {
            if (flag) {
                sb1 += to_string(i);
            } else {
                sb2 += to_string(i);
            }
            flag = !flag;
        }
        
        int i = sb1.size() - 1, j = sb2.size() - 1, carry = 0;
        
        // Add the two strings sb1 and sb2 from right to left
        while (i >= 0 || j >= 0 || carry == 1) {
            int val1 = i >= 0 ? sb1[i] - '0' : 0;
            int val2 = j >= 0 ? sb2[j] - '0' : 0;
            int sum = val1 + val2 + carry;
            carry = sum / 10;
            ans += (sum % 10) + '0';
            i--;
            j--;
        }
        
        // Reverse the result since it was built in reverse order
        reverse(ans.begin(), ans.end());
        
        // Remove leading zeros
        int z = 0;
        while (z < ans.size() && ans[z] == '0') {
            z++;
        }
        
        return ans.substr(z);
    }
};

