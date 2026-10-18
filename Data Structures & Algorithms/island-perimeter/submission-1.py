class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        visited = set()

        def dfs(i,j):
            if i < 0 or i>= rows or j <0 or j >= columns or grid[i][j] == 0:
                return 1
            
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            length = dfs(i+1,j) + dfs(i, j+1) + dfs(i-1,j) + dfs(i,j-1)

            return length
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    return dfs(i,j)
        
        