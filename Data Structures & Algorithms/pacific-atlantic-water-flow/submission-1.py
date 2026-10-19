class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        columns = len(heights[0])
        
        pacific_queue = deque()
        pacific_seen = set()

        atlantic_queue = deque()
        atlantic_seen = set()
        
        for i in range(rows):
            pacific_seen.add((i,0))
            pacific_queue.append((i,0))

            atlantic_queue.append((i,columns-1))
            atlantic_seen.add((i,columns-1))
        
        for i in range(columns):
            pacific_seen.add((0,i))
            pacific_queue.append((0,i))

            atlantic_queue.append((rows-1,i))
            atlantic_seen.add((rows-1,i))

        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def helper(queue, seen):
            while queue:
                i, j = queue.popleft()
                for x,y in directions:
                    new_i, new_j = i+x, j+y

                    if 0<= new_i < rows and 0<=new_j < columns and heights[new_i][new_j] >= heights[i][j] and (new_i, new_j) not in seen:
                        seen.add((new_i,new_j))
                        queue.append((new_i, new_j))
            return seen
        
        pacific = helper(pacific_queue, pacific_seen)
        atlantic = helper(atlantic_queue, atlantic_seen)

        answer = []

        for p in pacific:
            if p in atlantic:
                answer.append(p)
        
        return answer





        


    
    



