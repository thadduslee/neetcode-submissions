class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, cur_sum):
            if i == len(nums) and cur_sum == target:
                return 1

            if i == len(nums) and cur_sum != target:
                return 0
            
            if i >= len(nums):
                return 0
            
            else:
                return dfs(i+1, cur_sum + nums[i]) + dfs(i+1, cur_sum - nums[i])
        return dfs(0,0)
