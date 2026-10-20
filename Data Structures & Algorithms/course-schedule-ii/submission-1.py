class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for course, prereq in prerequisites:
            adj[prereq].append(course)
        
        state = [0] * numCourses
        answer = []

        def has_cycle(i):
            if state[i] == 2:
                return False
            
            if state[i] == 1:
                return True
        
            state[i] = 1
            
            for neighbour in adj[i]:
                if has_cycle(neighbour):
                    return True
            
            state[i] = 2
            answer.append(i)
            return False

        for i in range(numCourses):
            if has_cycle(i):
                return []
        
        return answer[::-1]

