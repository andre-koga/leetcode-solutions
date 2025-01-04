class Solution {
    public int lengthOfLongestSubstring(String s) {
        int bestL = 0;
        int currS = 0;
        for (int i = 0; i < s.length(); i++) {
            int relIndex = s.substring(currS, i).indexOf(s.charAt(i));
            if (relIndex != -1) {
                if (bestL < i - currS) {
                    bestL = i - currS;
                }
                currS = currS + relIndex + 1;
            } else if (i == s.length() - 1) {
                if (bestL < i + 1 - currS) {
                    bestL = i + 1 - currS;
                }
            }
        }

        return bestL;
    }
}