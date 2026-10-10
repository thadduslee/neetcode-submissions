class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def helper(i):
            count = 0
            for pile in piles:
                count += math.ceil(pile/i)
            if count <= h:
                return True
            return False
        
        low = 1
        high = max(piles)
        result = high
        while low <= high:
            mid = (high+low)//2
            if helper(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result

