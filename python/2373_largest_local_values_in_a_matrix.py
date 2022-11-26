class Solution:
    
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res_size = len(grid) - 2
        res = [ [0] * res_size for _ in range(res_size) ]

        for row in range(res_size):
            for col in range(res_size):
                res[row][col] = max(max(grid[row][col:col+3]), max(grid[row+1][col:col+3]), max(grid[row+2][col:col+3]))
        return res
