class Solution {
    public int myAtoi(String s) {
        s = s.trim();

        if (s.length() == 0) {
            return 0;
        }

        boolean ignoreFirst = s.charAt(0) == '-' || s.charAt(0) == '+';
        boolean neg = s.charAt(0) == '-';

        int result = 0;
        int i = ignoreFirst ? 1 : 0;
        while (i < s.length()) {
            if (Character.isDigit(s.charAt(i))) {
                int newNum = s.charAt(i) - '0';
                boolean[] breakIt = { false };
                result = clampIt(result, neg, newNum, breakIt);
                if (breakIt[0]) {
                    break;
                }
            } else {
                break;
            }
            i++;
        }

        return result;
    }

    private int clampIt(int result, boolean neg, int newDigit, boolean[] breakIt) {
        if (neg && (result < Integer.MIN_VALUE / 10 || result * 10 < Integer.MIN_VALUE + newDigit)) {
            breakIt[0] = true;
            return Integer.MIN_VALUE;
        } else if (neg) {
            return result * 10 - newDigit;
        } else if (result > Integer.MAX_VALUE / 10 || result * 10 > Integer.MAX_VALUE - newDigit) {
            breakIt[0] = true;
            return Integer.MAX_VALUE;
        } else {
            return result * 10 + newDigit;
        }
    }
}