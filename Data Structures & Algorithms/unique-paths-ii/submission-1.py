class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        def dfs(i,j):
            if i >= m or j >=n:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i == m-1 and j == n-1:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            
            count = dfs(i+1, j) + dfs(i, j+1)
            memo[(i,j)] = count
            return count
        return dfs(0,0)