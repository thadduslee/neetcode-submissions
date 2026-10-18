class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        columns = len(grid[0])

        visited = set()

        def dfs(i,j):
            if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j] == 0:
                return 0
            
            if (i,j) in visited:
                return 0
            
            visited.add((i,j))

            return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)
        

        maximum = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1 and (i,j) not in visited:
                    area = dfs(i,j)
                    maximum = max(maximum,area)
        
        return maximum