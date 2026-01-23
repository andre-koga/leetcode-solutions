# wait this question is way too easy wtf
# and some ppl are doing dynamic programming on it? why??

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m x n means we go right (n - 1) times and down (m - 1) times
        # so we have a total of (m + n - 2) moves, and any unique combination of
        # R and D is a different path.

        # m + n - 2 spots to put n - 1 balls. That's simple combinatorics:
        # first ball can be put in m + n - 2 spots
        # second ball can be put in m + n - 3 spots
        # ... last ball can be put in 1 spot
        # then we divide this by (n - 1)!
        # so total is just
        # (m + n - 2)! / (n - 1)!
        import math

        return math.comb(m + n - 2, n - 1)
