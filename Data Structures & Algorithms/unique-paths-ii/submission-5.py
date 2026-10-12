class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}

        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])

        def helper(i,j):
            if i < rows and j < columns:
                if obstacleGrid[i][j] == 1:
                    return 0

            if i == rows-1 and j == columns-1:
                return 1
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            if i == rows-1:
                return helper(i, j+1)
            
            if j == columns-1:
                return helper(i+1,j)
            

            
            memo[(i,j)] = helper(i+1,j) + helper(i,j+1)
            return memo[(i,j)]
        
        return helper(0,0)