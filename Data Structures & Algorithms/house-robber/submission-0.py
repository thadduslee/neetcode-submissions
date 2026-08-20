class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])

        def backtrack(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(nums[i] + backtrack(i-2), backtrack(i-1))
                return memo[i]
        return backtrack(len(nums)-1)