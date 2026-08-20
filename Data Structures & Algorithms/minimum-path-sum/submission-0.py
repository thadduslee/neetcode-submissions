class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        m = len(grid)
        n = len(grid[0])
        def dfs(i,j, cur_sum):
            if i == m -1 and j == n-1:
                return grid[i][j]
            
            elif i >= m or j >= n:
                return float("inf")
            
            if (i,j) in memo:
                return memo[(i,j)]
            count = min(dfs(i+1, j, cur_sum+grid[i][j]), dfs(i, j+1, cur_sum+grid[i][j]))
            count += grid[i][j]

            memo[(i,j)] = count
            return count
        return dfs(0,0, grid[0][0])
            