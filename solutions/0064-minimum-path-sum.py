# i mean, this is too easy rly

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp easy
        rowCount = len(grid)
        colCount = len(grid[0])

        dp = [[0] * colCount for _ in range(rowCount)]

        dp[0][0] = grid[0][0]

        for row in range(1, rowCount):
            dp[row][0] = dp[row - 1][0] + grid[row][0]

        for col in range(1, colCount):
            dp[0][col] = dp[0][col - 1] + grid[0][col]

        for row in range(1, rowCount):
            for col in range(1, colCount):
                top = dp[row - 1][col]
                left = dp[row][col - 1]
                dp[row][col] = grid[row][col] + (top if top < left else left)
        
        return dp[-1][-1]
