class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        degrees = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            degrees[course] +=1
        
        queue = deque()
        for i in range(numCourses):
            if degrees[i] == 0:
                queue.append(i)
        
        answer = []
        taken = 0 

        while queue:
            node = queue.popleft()
            answer.append(node)
            taken +=1

            for neighbour in adj[node]:
                degrees[neighbour] -=1

                if degrees[neighbour] == 0:
                    queue.append(neighbour)
        
        if taken == numCourses:
            return answer
        return []