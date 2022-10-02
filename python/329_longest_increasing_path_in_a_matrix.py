class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        num_row, num_col = len(matrix), len(matrix[0])
        dp = {} # (row, col) -> LIP
        
        def dfs(row, col, prev_val):
            if row < 0 or row == num_row or col < 0 or col == num_col or matrix[row][col] <= prev_val:
                return 0

            if (row,col) in dp:
                return dp[(row,col)]

            res = 1
            res = max(res, 1+dfs(row+1, col, matrix[row][col]))
            res = max(res, 1+dfs(row-1, col, matrix[row][col]))
            res = max(res, 1+dfs(row, col+1, matrix[row][col]))
            res = max(res, 1+dfs(row, col-1, matrix[row][col]))

            dp[(row,col)] = res
            
            return res

        for r in range(num_row):
            for c in range(num_col):
                dfs(r, c, -1)
        return max(dp.values())
