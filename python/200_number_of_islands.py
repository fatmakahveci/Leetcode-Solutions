class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def is_valid(row_col):
            row, col = row_col
            if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == '1' and (row,col) not in visited:
                return True
            return False
        
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [ [0,-1], [0,1], [-1,0], [1,0]]
        q = deque()
        visited = set()
        num_islands = 0
        
        def bfs(r,c):
            q.append((r,c))
            visited.add((r,c))
            while q:
                r,c = q.popleft()
                for direction in DIRECTIONS:
                    x = r + direction[0]
                    y = c + direction[1]
                    if is_valid((x,y)):
                        q.append((x,y))
                        visited.add((x,y))
                        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    num_islands += 1

        return num_islands
