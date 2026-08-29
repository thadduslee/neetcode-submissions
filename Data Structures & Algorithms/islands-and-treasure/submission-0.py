class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        columns = len(grid[0])
        
        visit = set()
        queue = deque()

        def helper(row, column):
            if row < 0 or column < 0 or row == rows or column == columns or grid[row][column] == -1 or (row,column) in visit:
                return
            
            visit.add((row,column))
            queue.append([row,column])
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0:
                    visit.add((i,j))
                    queue.append([i,j])
        
        distance = 0
        while queue:
            for i in range(len(queue)):
                row,column = queue.popleft()
                grid[row][column] = distance
                helper(row+1, column)
                helper(row-1, column)
                helper(row, column+1)
                helper(row, column-1)
            distance +=1


