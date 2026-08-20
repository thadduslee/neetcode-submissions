class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_queue = deque()
        p_seen = set()

        a_queue = deque()
        a_seen = set()

        m, n = len(heights), len(heights[0])

        for i in range(m):
            p_queue.append((i,0))
            p_seen.add((i,0))
        
        for j in range(1, n):
            p_queue.append((0,j))
            p_seen.add((0,j))
        
        for i in range(m):
            a_queue.append((i, n-1))
            a_seen.add((i, n-1))
        
        for j in range(n-1):
            a_queue.append((m-1, j))
            a_seen.add((m-1, j))
        
        def helper(queue, seen):
            while queue:
                i,j = queue.popleft()
                for i_offset, j_offset in [(0,1), (1,0), (0,-1), (-1,0)]:
                    i_new = i + i_offset
                    j_new = j + j_offset
                    if 0<= i_new < m  and 0<= j_new < n and heights[i][j] <= heights[i_new][j_new] and (i_new,j_new) not in seen:
                        seen.add((i_new,j_new))
                        queue.append((i_new,j_new))
            return seen
                    

        p_coords = helper(p_queue, p_seen)
        a_coords = helper(a_queue, a_seen)

        answer = []

        for coord in p_coords:
            if coord in a_coords:
                answer.append(coord)
        return answer