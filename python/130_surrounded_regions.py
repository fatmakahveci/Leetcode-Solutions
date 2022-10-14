class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(r, c):
            if r < 0 or c < 0 or c == n_col or r == n_row or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
                
        
        n_row, n_col = len(board), len(board[0])

        for row in range(n_row):
            for col in range(n_col):
                if board[row][col] == 'O' and (row == 0 or row == n_row-1 or col == 0 or col == n_col-1):
                    dfs(row, col)
        for row in range(n_row):
            for col in range(n_col):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
        for row in range(n_row):
            for col in range(n_col):
                if board[row][col] == 'T':
                    board[row][col] = 'O'
        return board
        
