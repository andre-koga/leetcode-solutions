# ummm what is this goofy problem?

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        result = ["." * n]
        other = ["#" * (n - 1) + "."] * (m - 1)
        result.extend(other)

        return result
