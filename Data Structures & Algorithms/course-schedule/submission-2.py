class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        
        state = [0] * numCourses

        def has_cycle(i):
            if state[i] == 1:
                return True
            
            if state[i] == 2:
                return False
            
            state[i] = 1

            for neighbour in adj[i]:
                if has_cycle(neighbour):
                    return True
            state[i] = 2
            return False 
        
        for i in range(numCourses):
            if has_cycle(i):
                return False
        
        return True