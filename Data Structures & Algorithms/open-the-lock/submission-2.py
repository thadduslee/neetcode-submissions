class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        if "0000" in deadends:
            return -1
        
        queue = deque([("0000", 0)])
        visited = {"0000"}
    
        while queue:
            number, turns = queue.popleft()

            if number == target:
                return turns
            
            for i in range(4):
                num = int(number[i])

                num_up = (num + 1)%10

                number_up = number[:i] + str(num_up) + number[i+1:]

                num_down = (num - 1)%10

                number_down = number[:i] + str(num_down) + number[i+1:]

                if number_up not in visited and number_up not in deadends:
                    queue.append((number_up, turns+1))
                    visited.add(number_up)
                
                if number_down not in visited and number_down not in deadends:
                    queue.append((number_down, turns+1))
                    visited.add(number_down)
        return -1