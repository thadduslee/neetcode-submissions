class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        columns = len(grid[0])

        queue = deque()
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0:
                    queue.append([i,j])
        
        directions= [[0,1], [0,-1], [1,0], [-1,0]]
        visited = set()
        while queue:
            row, column = queue.popleft()
            visited.add((row,column))
            for x,y in directions:
                new_row, new_column = row+x, column+y
                if new_row < 0 or new_column < 0 or new_row == rows or new_column == columns:
                    continue
                if (new_row, new_column) in visited:
                    continue
                if grid[new_row][new_column] == 2147483647:
                    queue.append([new_row, new_column])
                    grid[new_row][new_column] = 1 + grid[row][column]
        
        
            


