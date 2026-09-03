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
                digit = str((int(lock[i]) + 1) % 10)
                number1 = lock[:i] + digit + lock[i+1:]
                digit = str((int(lock[i]) - 1) % 10)
                number2 = lock[:i] + digit + lock[i+1:]
                res.append(number1)
                res.append(number2)
            return res
        
        q = deque()
        visited = set(deadends)
        q.append((start,0))
        while q:
            lock, num = q.popleft()
            visited.add(lock)
            if lock == target:
                return num
            
            for child in helper(lock):
                if child not in visited:
                    visited.add(child)
                    q.append((child, num+1))
        return -1




            
