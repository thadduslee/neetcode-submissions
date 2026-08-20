class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"
        if start in deadends:
            return -1
        
        if start == target:
            return 0
        
        def helper(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1)%10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit2 = str((int(lock[i]) - 1)%10)
                res.append(lock[:i] + digit2 + lock[i+1:])
            return res
        
        q = deque()
        visited = set(deadends)
        q.append((start, 0)) #lock, turns
    
        while q:
            lock, turns = q.popleft()
            visited.add(lock)
            if lock == target:
                return turns
            for child in helper(lock):
                if child not in visited:
                    visited.add(child)
                    q.append((child, turns +1))
            
        return -1