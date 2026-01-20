class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # attempt at coding the standard approach for this problem:
        # (just read the idea, didn't see solution)

        # backtracking while tracking column, posdiag and negdiag
        # wow i did it, and it was pretty easy too
        self.results = []
        self.solve(set(), set(), set(), [], n)

        return self.results

    def solve(self, cols, pdiags, ndiags, queens, n):
        row = len(queens)
        if row >= n:
            board = [["."] * n for _ in range(n)]
            for queen in queens:
                board[queen[0]][queen[1]] = "Q"
            for i in range(n):
                board[i] = "".join(board[i])
            self.results.append(board)
            return
        
        # check all spots in this row
        for i in range(n):
            pdiag = row + i
            ndiag = row - i
            if i not in cols and pdiag not in pdiags and ndiag not in ndiags:
                cols.add(i)
                pdiags.add(pdiag)
                ndiags.add(ndiag)
                queens.append((row, i))

                self.solve(cols, pdiags, ndiags, queens, n)

                # now remove
                cols.remove(i)
                pdiags.remove(pdiag)
                ndiags.remove(ndiag)
                queens.pop()
