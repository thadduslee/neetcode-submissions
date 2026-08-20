class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def works(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            return hours <= h
        low, high = 1, max(piles)
        smallest = max(piles)
        while low<=high:
            mid = (high-low)//2 + low
            if works(mid):
                smallest = mid
                high = mid - 1
            else:
                low = mid + 1
        return smallest
