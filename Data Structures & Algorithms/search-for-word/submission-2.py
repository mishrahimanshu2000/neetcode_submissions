class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[False] * n for _ in range(m)]
        
        def isValid(r,c):
            return 0 <= r < m and 0 <= c < n

        def helper(r,c,idx):
            if idx == len(word):
                return True
            
            if not isValid(r,c) or board[r][c] != word[idx] or visited[r][c]:
                return False
            
            visited[r][c] = True
            
            for i in range(4):
                if helper(r+dirs[i][0], c+dirs[i][1],idx+1):
                    return True
            
            visited[r][c] = False
            return False
        
        for i in range(m):
            for j in range(n):
                if helper(i,j,0):
                    return True
        
        return False

