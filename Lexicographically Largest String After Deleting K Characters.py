class Solution {
  public:
    string maxSubseq(string& s, int k) {
        int n = s.size();
        int keep = n - k;
        string stack = "";

        for (char c : s) {
            while (!stack.empty() && k > 0 && stack.back() < c) {
                stack.pop_back();
                k--;
            }
            stack.push_back(c);
        }

        // Only keep the required number of characters
        return stack.substr(0, keep);
    }
};
