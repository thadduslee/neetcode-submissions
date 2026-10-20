class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target in deadends or "0000" in deadends:
            return -1
        
        minimum = float('inf')
        queue = deque([("0000",0)])
        visited = {"0000"}
        deadends = set(deadends)

        while queue:
            number, turn = queue.popleft()

            if number == target:
                return turn
            
            
            for i in range(4):
                num = int(number[i])

                num_up = (num + 1)%10
                number_up = number[:i] + str(num_up) + number[i+1:]

                num_down = (num-1)%10
                number_down = number[:i] + str(num_down) + number[i+1:]

                if number_up not in deadends and number_up not in visited:
                    visited.add(number_up)
                    queue.append((number_up, turn+1))

                if number_down not in deadends and number_down not in visited:
                    visited.add(number_down)
                    queue.append((number_down, turn+1))
        return -1
