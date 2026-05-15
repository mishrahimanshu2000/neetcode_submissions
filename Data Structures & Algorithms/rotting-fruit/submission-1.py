class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))
                
        if fresh == 0:
            return 0
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        ans = -1
        while q:
            size = len(q)
            for _ in range(size):
                r,c = q.popleft()
                for dr,dc in dirs:
                    nr = r+dr
                    nc = c+dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            ans += 1
        if fresh == 0:
            return ans
        return -1