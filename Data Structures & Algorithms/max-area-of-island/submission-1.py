class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r,c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 1:
                return 0
            sz = 1 
            grid[r][c] = 2
            for dr, dc in dirs:
                sz += dfs(r+dr,c+dc)

            return sz
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i,j))
        return res          