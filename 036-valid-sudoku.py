# solution beats 75% of submissions in time and 70% on space
# honestly i could've just mashed the three tests into a single one and just check for len != count
# but this is also fine, perhaps a bit more obvious to the untrained eye

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows first
        for i in range(9):
            nums = set()
            total = 0
            for j in range(9):
                if board[i][j] != ".":
                    total += 1
                    nums.add(board[i][j])
            if total != len(nums):
                return False
        
        # check columns now, same thing
        for i in range(9):
            nums = set()
            total = 0
            for j in range(9):
                if board[j][i] != ".":
                    total += 1
                    nums.add(board[j][i])
            if total != len(nums):
                    return False
        
        # check 3x3s
        for i in range(3):
            for j in range(3):
                nums = set()
                total = 0
                for a in range(3):
                    for b in range(3):
                        if board[i * 3 + a][j * 3 + b] != ".":
                            total += 1
                            nums.add(board[i * 3 + a][j * 3 + b])
                if total != len(nums):
                    return False

        return True