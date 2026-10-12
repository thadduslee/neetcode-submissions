class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def helper(remain):
            if remain == 0:
                return 1
            if remain < 0:
                return 0
            if remain in memo:
                return memo[remain]

            ways = 0
            for num in nums:
                ways += helper(remain - num)
            
            memo[remain] = ways
            return ways
        helper(target)
        return memo[target]
