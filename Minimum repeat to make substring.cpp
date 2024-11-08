class Solution {
  public:
    int minRepeats(std::string& s1, std::string& s2) {
        std::string repeated_s1 = s1;
        int count = 1;
        
        // Repeat s1 until its length is at least as long as s2
        while (repeated_s1.size() < s2.size()) {
            repeated_s1 += s1;
            count++;
        }
        
        // Check if s2 is a substring of the current repeated s1
        if (repeated_s1.find(s2) != std::string::npos) {
            return count;
        }
        
        // Check by adding one more repetition to cover cross-boundary cases
        repeated_s1 += s1;
        if (repeated_s1.find(s2) != std::string::npos) {
            return count + 1;
        }
        
        // If s2 is still not a substring, return -1
        return -1;
    }
};
