# 0ms? It says that it beats 100% of all solutions.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # first reaction: is this going to be O(n)?
        # if so, let's do it the stupid way

        width = len(matrix[0])
        height = len(matrix)

        curX = -1
        curY = 0

        output = []

        while True:
            for _ in range(width):
                print("right")
                curX += 1
                output.append(matrix[curY][curX])
            
            if width == 0:
                break
            height -= 1

            for _ in range(height):
                print("down")
                curY += 1
                output.append(matrix[curY][curX])

            if height == 0:
                break
            width -= 1

            for _ in range(width):
                print("left")
                curX -= 1
                output.append(matrix[curY][curX])

            if width == 0:
                break
            height -= 1

            for _ in range(height):
                print("up")
                curY -= 1
                output.append(matrix[curY][curX])
            
            if height == 0:
                break
            width -= 1

        return output
                