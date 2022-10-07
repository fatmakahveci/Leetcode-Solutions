class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix[0])
        
        for i in range(n//2+n%2):
            for j in range(n//2):
                temp = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = matrix[i][j]
                matrix[i][j] = temp
