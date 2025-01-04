# recursive original solution for the problem count and say
# nothing that clever in this one, but it was better than 50% of submissions
# (so right in the middle)


class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 1:
            return "1"
        
        prior = self.countAndSay(n - 1)
        n = len(prior)
        result = ""

        i = 0
        count = 0
        digit = ""
        while i < n:
            digit = prior[i]
            count = 1
            while i + count < n and prior[i + count] == digit:
                count += 1
            result += str(count) + digit
            i += count
        
        return result