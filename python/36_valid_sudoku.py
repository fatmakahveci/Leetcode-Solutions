class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        N = 9

        for r in range(N):
            rows = [c for c in board[r] if c != '.']
            if len(rows) != len(set(rows)): return False

        for c in range(N):
            cols = [board[r][c] for r in range(N) if board[r][c] != '.']
            if len(cols) != len(set(cols)): return False
        
        def check_each_box(row, col):
            numbers_in_box = set()
            for r in range(row, row+3):
                for c in range(col, col+3):
                    if board[r][c] == '.': continue
                    if board[r][c] not in numbers_in_box:
                        numbers_in_box.add(board[r][c])
                    else:
                        return False
            return True
        
        for r in range(0, N, 3):
            for c in range(0, N, 3):
                if not check_each_box(r, c): return False

        return True
