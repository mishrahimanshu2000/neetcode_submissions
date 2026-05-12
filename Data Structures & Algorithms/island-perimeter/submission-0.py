class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = [0]
        dirs = [(0,1),(0,-1),(-1,0),(1,0)]
        def dfs(r,c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 0:
                return 1
            if grid[r][c] != 1:
                return 0
            grid[r][c] = 2

            pari = 0
            for dr, dc in dirs:
                pari += dfs(r+dr,c+dc)
            
            return pari
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(i,j)
            
            
        return 0