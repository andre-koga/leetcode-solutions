# very slow lol, but it works. i'll keep it for now. i'll try to make it faster later.

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if x == -1:
            return 1 if n % 2 == 0 else -1
        if x == 1:
            return 1
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        
        result = x
        powTotal = 1

        # powers of two to be faster
        while powTotal * 2 < n and result != 0:
            result *= result
            powTotal *= 2
        
        # now we do the rest
        n -= powTotal
        while n > 0 and result != 0:
            result *= x
            n -= 1
        
        # if odd then do 2nd method and go back to evens
        # if even then do 1st quick method
        # ill keep my old solution bc i didnt come up with the cool faster method

        return result