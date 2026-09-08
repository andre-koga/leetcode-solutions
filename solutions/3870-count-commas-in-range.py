# bro what is this question lmao

class Solution:
    def countCommas(self, n: int) -> int:
        # for any n <= 999 we get 0
        # for any n < 999,999 we get 1
        
        # in the constraints, n <= 10^5 = 100,000

        if n < 1000:
            return 0
        else:
            return n - 999
