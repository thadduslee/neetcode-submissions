class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def helper(i,j):
            if i == m-1 and j == n-1:
                return 1
            
            if i == m-1:
                return helper(i, j+1)
            
            if j == n-1:
                return helper(i+1, j)

            if i == m or j == n:
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            total = helper(i+1, j) + helper(i, j+1)

            memo[(i,j)] = total
            return memo[(i,j)]
        
        return helper(0,0)
        

            