class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        sq_matrix = [[0]*(n+1) for i in range(m+1)]
        max_sq = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1] == "1":
                    sq_matrix[i][j] = min(sq_matrix[i-1][j-1], sq_matrix[i-1][j], sq_matrix[i][j-1]) + 1
                    max_sq = max(max_sq, sq_matrix[i][j])
        return max_sq**2
