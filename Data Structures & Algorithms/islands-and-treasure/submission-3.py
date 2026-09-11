class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647

        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))
        curr = 0
        while q:
            n = len(q)
            curr += 1
            for _ in range(n):
                r,c = q.popleft()
                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                for dr,dc in directions:
                    row, col = r+dr, c+dc
                    if row >= 0 and row < ROWS and col >= 0 and col < COLS and grid[row][col] == INF:
                        grid[row][col] = curr
                        q.append((row, col))

                    
        