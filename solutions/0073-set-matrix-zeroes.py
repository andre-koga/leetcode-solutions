class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # my concern is to avoid new zeroes to not be mixed with the true
        # source zeroes.
        # i could do two passes, the first finds all the zeroes
        # the second sets the necessary numbers to zeroes
        # O(mn)
        # constant space solution, mmmmm....
        # i'll just settle for O(m + n) for now
        rows = set()
        cols = set()

        rowCount = len(matrix)
        colCount = len(matrix[0])

        for row in range(rowCount):
            for col in range(colCount):
                if matrix[row][col] == 0:
                    rows.add(row)
                    cols.add(col)

        for row in rows:
            matrix[row] = [0] * colCount
        
        for col in cols:
            for row in range(rowCount):
                matrix[row][col] = 0

        # bro the constant space solution is so goofy
