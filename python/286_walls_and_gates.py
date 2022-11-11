class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        wall = -1
        gate = 0
        empty = 2147483647
        
        directions = [ [1,0], [-1,0], [0,1], [0,-1] ]
        
        m, n = len(rooms), len(rooms[0])
        queue = []
        for row in range(m):
            for col in range(n):
                if rooms[row][col] == gate:
                    queue.append([row, col])
        
        while queue:
            row, col = queue.pop(0)
            for direction in directions:
                curr_row = row + direction[0]
                curr_col = col + direction[1]
                
                if curr_row < 0 or curr_row >= m or curr_col < 0 or curr_col >= n or rooms[curr_row][curr_col] != empty:
                    continue
                rooms[curr_row][curr_col] = rooms[row][col] + 1
                queue.append([curr_row, curr_col])
