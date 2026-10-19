class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rows = len(grid)
        columns = len(grid[0])
        queue = deque()
        visited = set()

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    fresh +=1
                
                if grid[i][j] == 2:
                    queue.append((i,j))
                    visited.add((i,j))
        if fresh == 0:
            return 0
        time = 0

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while queue:
            level_size = len(queue)

            for temp in range(level_size):
                i,j = queue.popleft()
                for x,y in directions:
                    new_i, new_j = i+x, j+y

                    if 0<=new_i<rows and 0<=new_j < columns and grid[new_i][new_j] == 1 and (new_i, new_j) not in visited:
                        visited.add((new_i, new_j))
                        fresh -=1
                        queue.append((new_i, new_j))
            time +=1
            if fresh == 0:
                return time
        if fresh == 0:
            return time
        return -1




        
