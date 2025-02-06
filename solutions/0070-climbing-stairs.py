# easy fibonacci problem. beats 100% at 0ms

class Solution:
    def climbStairs(self, n: int) -> int:
        # the quantity at n Q(n) = Q(n-1) + Q(n-2). wait this is just fibonacci
        if n <= 3:
            return n
        
        # Q(1) = 1 Q(2) = 2 Q(3) = 3 Q(4) = 5...
        prev = 2
        curr = 3
        for _ in range(n - 3):
            curr, prev = curr + prev, curr

        return curr