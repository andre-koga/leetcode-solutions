# beats 100%, but not completely original.

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # reflect diagonally
        n = len(matrix)

        if n <= 1:
            return
        
        # [a][b] goes to [b][a] and vice versa
        for x in range(n):
            for y in range(x, n):
                if x != y:
                    matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

        # reflect thru y axis
        for x in range(n):
            for y in range(n // 2):
                matrix[x][y], matrix[x][n - y -1] = matrix[x][n - y -1], matrix[x][y]