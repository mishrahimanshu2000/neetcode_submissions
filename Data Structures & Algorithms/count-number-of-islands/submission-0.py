class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dr = [0,0,1,-1]
        dc = [1,-1,0,0]
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
                return 
            grid[r][c] = '2'
            for i in range(4):
                dfs(r+dr[i], c+dc[i])
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands+=1
                    dfs(i,j)
        return islands
                 