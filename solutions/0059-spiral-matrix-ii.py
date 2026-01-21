# completely original solution! (tbf this is a medium question that isn't hard at all)

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # brute force?
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_dir = 0
        result = [[0] * n for _ in range(n)]

        count = 0
        total = n ** 2
        row, col = 0, 0
        while count < total:
            count += 1
            result[row][col] = count

            # move forward
            new_row = row + dirs[curr_dir][0]
            new_col = col + dirs[curr_dir][1]
            oob = new_row < 0 or new_row >= n or new_col < 0 or new_col >= n
            if oob or result[new_row][new_col] != 0:
                # change dirs and get proper direction
                curr_dir = curr_dir + 1 if curr_dir < 3 else 0
                new_row = row + dirs[curr_dir][0]
                new_col = col + dirs[curr_dir][1]

            row, col = new_row, new_col

        return result
