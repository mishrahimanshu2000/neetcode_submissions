class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(0,1),(0,-1),(-1,0),(1,0)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 4

                    for dr, dc in dirs:
                        nr = i + dr
                        nc = j + dc
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                            res -= 1
                    
        return res