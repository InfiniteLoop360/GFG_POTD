class Solution {
    public String smallestWindow(String s, String p) {
        if (s.isEmpty() || p.isEmpty() || p.length() > s.length()) {
            return "-1";
        }

        Map<Character, Integer> charCount = new HashMap<>();
        for (char c : p.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }

        int required = charCount.size();
        int left = 0, right = 0, formed = 0;
        Map<Character, Integer> windowCounts = new HashMap<>();

        int minLength = Integer.MAX_VALUE;
        int minLeft = 0;

        while (right < s.length()) {
            char c = s.charAt(right);
            windowCounts.put(c, windowCounts.getOrDefault(c, 0) + 1);

            if (charCount.containsKey(c) && windowCounts.get(c).equals(charCount.get(c))) {
                formed++;
            }

            while (left <= right && formed == required) {
                c = s.charAt(left);

                if (right - left + 1 < minLength) {
                    minLength = right - left + 1;
                    minLeft = left;
                }

                windowCounts.put(c, windowCounts.get(c) - 1);
                if (charCount.containsKey(c) && windowCounts.get(c) < charCount.get(c)) {
                    formed--;
                }

                left++;
            }

            right++;
        }

        return minLength == Integer.MAX_VALUE ? "-1" : s.substring(minLeft, minLeft + minLength);
    }

    // Example usage
    public static void main(String[] args) {
        Solution solution = new Solution();
        String S1 = "timetopractice";
        String P1 = "toc";
        System.out.println(solution.smallestWindow(S1, P1));  // Output: "toprac"
    }
}
