class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        columns = len(grid[0])

        queue = deque()
        visited = set()
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))


        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            i,j = queue.popleft()
            
            for x,y in directions:
                new_i, new_j = i+x, j+y
                if 0 <= new_i < rows and 0 <= new_j < columns and grid[new_i][new_j] != -1 and (new_i,new_j) not in visited:
                    visited.add((new_i,new_j))
                    grid[new_i][new_j] = grid[i][j] +1
                    queue.append((new_i,new_j))





