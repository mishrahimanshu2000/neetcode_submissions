class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def isValid(r,c):
            return 0 <= r < m and 0 <= c < n

        def helper(r,c,idx):
            if idx == len(word):
                return True
            
            if not isValid(r,c) or board[r][c] != word[idx]:
                return False
            
            board[r][c] = '-'
            for i in range(4):
                if helper(r+dirs[i][0], c+dirs[i][1],idx+1):
                    return True
            
            board[r][c] = word[idx]
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and helper(i,j,0):
                    return True
        
        return False

