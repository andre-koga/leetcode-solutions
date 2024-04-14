# Solution and Explanation:

# If there's a valid sequence of size S,
# just insert "()" anywhere inside it to generate
# another valid sequence of size S+1.
# Store all of the new sequences of size S+1
# in a new set, then repeat. That's it.
# Now we just need to translate this into code:

# this solution beats 98% of all python3 submissions (time). It is really good.
# (original solution)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        n -= 1
        result = {"()"}

        while n > 0:
            newResult = set()
            for item in result:
                for i in range(len(item)):
                    newResult.add(item[:i] + "()" + item[i:])
            result = newResult
            n -= 1
        return result