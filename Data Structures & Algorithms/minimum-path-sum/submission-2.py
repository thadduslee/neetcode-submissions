class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        rows = len(grid)
        columns = len(grid[0])

        def helper(i,j):
            if i == rows-1 and j == columns-1:
                return grid[i][j]
            
            if i == rows-1:
                return grid[i][j] + helper(i, j+1)
            
            if j == columns-1:
                return grid[i][j] + helper(i+1, j)
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            memo[(i,j)] = grid[i][j] + min(helper(i+1,j), helper(i,j+1))
            return memo[(i,j)]
        
        return helper(0,0)
            