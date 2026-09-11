class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        curr = 1
        while q:
            n = len(q)
            for _ in range(n):
                r,c = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr,dc in directions: 
                    row, col = dr + r, dc + c
                    if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] != 2147483647:
                        continue
                    if curr < grid[row][col]:
                        grid[row][col] = curr 
                    q.append((row,col))
            curr += 1
        return