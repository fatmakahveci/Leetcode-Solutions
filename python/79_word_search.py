class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        board = A B C E
                S F C S
                A D E E

        f(0, 0, 'ABCCED') <= True -> f(0, 1, 'BCCED') <= True -> f(0, 2, 'CCED') <= True -> f(0, 3, 'CED') <= False
        board = A B C E      board = # B C E     board = # # C E -> f(1, 2, 'CED') <= True -> f(1, 3, 'ED') <= False   
                S F C S              S F C S             S F C S    board = # # # E -> f(2, 2, 'ED') -> f(2, 1, 'D') <= True
                A D E E              A D E E             A D E E            S F C S    board = # # # E  board = # # # E -> f(2, 2, '') <= True
                ...                  ...                 ...                A D E E            S F # S          S F # S
                                                                                               A D E E          A D # E
        '''
        
        def dfs(row, col, suffix):
            if len(suffix) == 0:
                return True

            if row < 0  or col < 0 or row == ROWS or col == COLS or board[row][col] != suffix[0]:
                return False

            ret = False
            board[row][col] = '#'

            for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ret = dfs( row+rowOffset, col+colOffset, suffix[1:] )
                if ret:
                    break

            board[row][col] = suffix[0]

            return ret

        ROWS, COLS = len(board), len(board[0])
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, word):
                    return True

        return False
