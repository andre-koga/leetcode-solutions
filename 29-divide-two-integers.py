# I really like this solution
# after checking the forum I saw a lot of solutions using range or other tricks to hide divisions / multiplications
# my solution doesn't use any tricks and still achieves logarithmic speeds.

# the core idea of the solution is the powers array, which stores 1, 1*divisor, 2*divisor, 4*divisor, etc.
# then we just check for which ones to use, and add the exponents to the q value.

# better than 83% of submissions! and i didn't even use bitshift.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor == 1:
            if dividend < 0:
                return max(dividend, -2147483648)
            else:
                return min(dividend, 2147483647)
        elif divisor == -1:
            if dividend < 0:
                return min(-dividend, 2147483647)
            else:
                return max(-dividend, -2147483648)

        neg = False
        if divisor < 0 and dividend < 0:
            divisor = -divisor
            dividend = -dividend
        elif divisor < 0 or dividend < 0:
            neg = True
            divisor = abs(divisor)
            dividend = abs(dividend)
        
        # both positive
        if divisor > dividend:
            return 0
        elif divisor == dividend:
            return -1 if neg else 1

        # divisor^index
        powers = [(0, 1), (1, divisor)]
        

        while powers[-1][1] + powers[-1][1] < dividend:
            powers.append((powers[-1][0] + powers[-1][0], powers[-1][1] + powers[-1][1]))

        q = 0
        while divisor <= dividend:
            idx = len(powers) - 1
            while powers[idx][1] > dividend:
                idx -= 1
            q += powers[idx][0]
            dividend -= powers[idx][1]

        return -q if neg else q