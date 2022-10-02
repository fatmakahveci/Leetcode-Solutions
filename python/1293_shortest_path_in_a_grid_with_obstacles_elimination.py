class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n_row, n_col = len(grid), len(grid[0])
        visited = set()
        q = [(0, 0, k, 0)] 
        while q:
            row, col, rem_obs, cnt_move = q.pop(0)
            if (row, col, rem_obs) in visited or rem_obs < 0:
                continue
            if (row, col) == (n_row-1, n_col-1):
                return cnt_move
            visited.add((row, col, rem_obs))
            if grid[row][col] == 1:
                rem_obs -= 1
            for d_row, d_col in [ (0,1), (0,-1), (1,0), (-1,0) ]:
                row_to_move = row + d_row
                col_to_move = col + d_col
                if 0 <= row_to_move < n_row and 0 <= col_to_move < n_col:
                    q.append((row_to_move, col_to_move, rem_obs, cnt_move+1))
        return -1
