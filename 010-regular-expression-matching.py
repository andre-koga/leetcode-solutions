# most default bottom up dp solution
# time: O(n*m)
# many yt videos on this

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # using dp
        slen = len(s)
        plen = len(p)

        dp = {}
        dp[(0, 0)] = True
        dp[(0, 1)] = False

        for i in range(1, slen + 1):
            dp[(i, 0)] = False
        
        for j in range(2, plen + 1):
            # this works bc the only way for a non empty pattern to
            # match an empty string is for every even character from
            # the pattern to equal *, allowing every odd character to
            # just be discarded.
            dp[(0, j)] = dp[(0, j - 2)] and p[j - 1] == '*'

        for i in range(1, slen + 1):
            for j in range(1, plen + 1):
                match = s[i - 1] == p[j - 1] or p[j - 1] == '.'
                
                if match:
                    dp[(i, j)] = dp[(i - 1, j - 1)]
                elif p[j - 1] == "*":
                    wildcard_match = s[i - 1] == p[j - 2] or p[j - 2] == '.'
                    dp[(i, j)] = dp[(i, j - 2)] or (dp[(i - 1, j)] if wildcard_match else False)
                else:
                    dp[(i, j)] = False

        return dp[(slen, plen)]