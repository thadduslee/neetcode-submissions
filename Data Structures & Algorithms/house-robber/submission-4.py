class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        maximum = [0] * (len(nums)+1)
        maximum[0] = nums[0]
        maximum[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            maximum[i] = max(maximum[i-2] + nums[i], maximum[i-1])
        return maximum[len(nums)-1]

        