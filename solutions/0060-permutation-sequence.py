# i cannot believe i solved this question in 20 minutes with no assistance
# the power of coffee is real

# tbf, this ain't hard. beats 100% with 0ms runtime

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        # the digit on the left is very easy to calculate:
        # for n digits, the digit on the left shows up
        # equal to the number of available permutations
        # to the numbers on the right, which is simply (n - 1)!
        # k // (n - 1)! + 1
        # we take it out, then repeat this process again but 
        # skipping the one we just used
        # 1234
        # 1243
        # 1324
        # 1342
        # 1423
        # 1432
        # 2134
        # 2143...
        # the number on the left shows up (2-1)! = 1 times
        digits = list(range(1, n + 1))
        
        result = []

        for i in range(n):
            digit = (k - 1) // math.factorial(n - i - 1)
            digit = digit % len(digits)
            result.append(str(digits[digit]))
            digits.remove(digits[digit])

        return "".join(result)
