class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                k = board[i][j]
                gI = (i//3) * 3 + (j//3)
                if k in row[i] or k in col[j] or k in grid[gI]:
                    return False
                row[i].add(k)
                col[j].add(k)
                grid[gI].add(k)
        return True