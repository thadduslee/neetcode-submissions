class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def helper(number):
            count = 1
            available = number

            for weight in weights:
                if available - weight >= 0:
                    available -= weight
                else:
                    count +=1
                    available = number - weight

            if count <= days:
                return True
            return False
        
        low = max(weights)
        highest = sum(weights)
        result = sum(weights)

        while low <= highest:
            mid = (highest + low)//2
            if helper(mid):
                result = mid
                highest = mid -1
            
            else:
                low = mid +1
        return result
            
