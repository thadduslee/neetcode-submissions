class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        answer = max(piles)
        low = 1
        high = max(piles)

        while low <= high:
            mid = (high+low)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile)/mid)
            if hours <= h:
                answer = mid
                high = mid -1
            else:
                low = mid + 1
            
        return answer
