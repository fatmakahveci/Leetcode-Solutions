class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        edit_distance_matrix = [ [0] * (n + 1) for i in range(m + 1) ]

        for row in range(m + 1):
            for column in range(n + 1):
                if row == 0:
                    edit_distance_matrix[row][column] = column
                elif column == 0:
                    edit_distance_matrix[row][column] = row
                elif word1[row - 1] == word2[column - 1]:
                    edit_distance_matrix[row][column] = edit_distance_matrix[row - 1][column - 1]
                else:
                    edit_distance_matrix[row][column] = 1 + min(edit_distance_matrix[row][column - 1],
                                                                edit_distance_matrix[row - 1][column],
                                                                edit_distance_matrix[row - 1][column - 1])
        return edit_distance_matrix[m][n]
