# solve using recursion / backtracking with mrv
# holy shit, without mrv it takes like 2000ms (2 secs)
# with mrv it takes 20ms
# not an original solution, I learned the strategy from the following video:
# https://www.youtube.com/watch?v=eAFcj_2quWI
# but then it kept timing out, so I implemented mrv as suggested by chatgpt

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    d = board[r][c]
                    self.rows[r].add(d)
                    self.cols[c].add(d)
                    self.boxes[(r // 3) * 3 + c // 3].add(d)
        
        self.empty = [(r, c) for r in range(9) for c in range(9) if board[r][c] == "."]
        self.solve(board, 0)

    def solve(self, board, i):
        if i >= len(self.empty):
            return True

        # use mrv
        best_i = i
        best_count = 10

        for j in range(i, len(self.empty)):
            r, c = self.empty[j]
            b = (r // 3) * 3 + c // 3
            count = 9 - len(self.rows[r] | self.cols[c] | self.boxes[b])

            if count < best_count:
                best_count = count
                best_i = j
                if count == 1:
                    break

        # flip
        self.empty[i], self.empty[best_i] = self.empty[best_i], self.empty[i]

        x, y = self.empty[i]
        b = (x // 3) * 3 + y // 3

        # didn't reach the end yet, keep going
        for d in "123456789":
            if self.is_valid(x, y, d):
                board[x][y] = d
                self.rows[x].add(d)
                self.cols[y].add(d)
                self.boxes[b].add(d)

                if self.solve(board, i + 1):
                    return True

                board[x][y] = "."
                self.rows[x].remove(d)
                self.cols[y].remove(d)
                self.boxes[b].remove(d)

        return False
    
    def is_valid(self, x, y, d):
        b = (x // 3) * 3 + y // 3
        return d not in self.rows[x] and d not in self.cols[y] and d not in self.boxes[b]
