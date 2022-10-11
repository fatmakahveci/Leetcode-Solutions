class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            temp_row = [0] + row + [0]
            row = []
            for j in range(i+2):
                row.append(temp_row[j]+ temp_row[j+1])
        return row
# 0: row: 1     temp: 0 1 0     row: 1 1
# 1: row: 1 1   temp: 0 1 1 0   row: 1 2 1
# 2: row: 1 2 1 temp: 0 1 2 1 0 row: 1 3 3 1
