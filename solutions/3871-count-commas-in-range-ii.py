class Solution:
    def countCommas(self, n: int) -> int:
        # < 1,000 = 10^3 give 0
        # < 1,000,000 = 10^6 give 1
        # < ... 10^(3n + 3) give n
        # the constraint goes up to 10^15 = 10^(3 * 4 + 3) gives 4

        ceiling = 1
        commas = 0
        while n >= ceiling * 1000:
            ceiling *= 1000
            commas += 1

        # ceiling is below n
        total = 0
        while commas > 0:
            total += commas * (n - ceiling + 1)
            commas -= 1
            n = ceiling - 1
            ceiling = ceiling // 1000

        return total
