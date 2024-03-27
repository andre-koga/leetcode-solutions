class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1 || numRows >= s.length()) {
            return s;
        }

        int pointer = 0;
        int currRow = 0;
        boolean increasing = true;
        int[] currIndex = new int[numRows];
        char[][] rows = new char[numRows][s.length() / numRows * 2];

        while (pointer < s.length()) {
            rows[currRow][currIndex[currRow]] = s.charAt(pointer);
            pointer++;
            currIndex[currRow]++;

            if (currRow == numRows - 1) {
                increasing = false;
            } else if (currRow == 0 && !increasing) {
                increasing = true;
            }

            currRow += (increasing ? 1 : -1);
        }

        StringBuilder res = new StringBuilder();

        int r = 0, p = 0;
        while (r < numRows) {
            p = 0;

            while (p < rows[r].length && (int) rows[r][p] != 0) {
                res.append(rows[r][p]);

                p++;
            }

            r++;
        }

        return res.toString();
    }
}