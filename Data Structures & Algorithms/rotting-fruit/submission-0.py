class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        fresh = 0
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh +=1
                elif grid[i][j] ==2:
                    q.append([i,j])
        
        def helper(i,j):
            nonlocal fresh
            if i<0 or j <0 or i>= m or j >= n or grid[i][j] != 1:
                return
            
            else:
                grid[i][j] = 2
                q.append([i,j])
                fresh -=1
        time = 0
        while q and fresh>0:
            x = len(q)
            for temp in range(x):
                i,j = q.popleft()
                helper(i+1, j)
                helper(i, j+1)
                helper(i-1, j)
                helper(i, j-1)
            time +=1
        if fresh == 0:
            return time
        else:
            return -1
