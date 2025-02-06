# beats 100% of solutions

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # naive - i know the question wants more, but why?:
        return str(bin(int(a, 2) + int(b, 2)))[2:]