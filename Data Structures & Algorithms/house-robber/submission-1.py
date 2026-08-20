class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [0] * len(nums)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            memo[i] = max(memo[i-1], memo[i-2] + nums[i])

        return memo[len(nums)-1]

        