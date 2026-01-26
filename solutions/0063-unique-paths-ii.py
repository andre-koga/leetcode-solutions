# original solution! (tho this isn't a hard question)
# beats 100% with an average runtime of 0ms despite the
# obvious O(m*n)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # the number of routes that the obstacle blocks is equal
        # to the number of routes that can even reach the obstacle
        # times the number of routes that can go from the obstacle to the end

        # so the obstacle can be seen as dividing the board into two
        # smaller boards, one on the topleft and another on the bottomright
        # which are identical to the solution from unique paths I

        # is it always 1 obstacle?
        # oh since it's not always 1 obstacle we gotta use DP...
        # dp[i][j] represents the number of paths that go to i, j:
        # the only way to reach i, j is to check i - 1, j and i, j - 1
        # and add both of them.
        # of course, if i, j is an obstacle then we set it to 0

        numRows = len(obstacleGrid)
        numCols = len(obstacleGrid[0])

        dp = [[0] * numCols for _ in range(numRows)]
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        dp[0][0] = 1

        for row in range(1, numRows):
            if obstacleGrid[row][0] == 1:
                break
            dp[row][0] = dp[row - 1][0]

        for col in range(1, numCols):
            if obstacleGrid[0][col] == 1:
                break
            dp[0][col] = dp[0][col - 1]
        
        for row in range(1, numRows):
            for col in range(1, numCols):
                if obstacleGrid[row][col] == 1:
                    continue
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        
        return dp[-1][-1]
