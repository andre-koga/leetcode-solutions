# i saw some hints and finally got this solution after blood sweat and tears
# only to see the 9ms solution and realize there was a much simpler, more elegant, and greedier approach

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # i tried doing recursion. which sucks. so i'll just use a 2D array of dimension
        # len(s) x len(p) in which arr[x][y] is a bool for whether s[:x] and p[:y] match or not

        # simplify * first
        isStar = False
        new_p = ""
        for i in range(len(p)):
            if isStar and p[i] == "*":
                continue
            else:
                new_p += p[i]
            isStar = p[i] == "*"

        p = new_p

        n = len(s)
        m = len(p)

        matrix = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        matrix[0][0] = True

        # setup only exception that occurs when first char is * in the pattern:
        for i in range(m):
            if p[i] == "*":
                matrix[0][i + 1] = True
            else:
                break

        for i in range(n):
            for j in range(m):
                if p[j] == "*":
                    matrix[i + 1][j + 1] = matrix[i][j + 1] or matrix[i + 1][j]
                elif p[j] == "?" or s[i] == p[j]:
                    matrix[i + 1][j + 1] = matrix[i][j]

        return matrix[n][m]
