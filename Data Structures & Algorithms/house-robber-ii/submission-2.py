class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0
        if len(nums) == 2:
            return max(nums[0], nums[1])
        #use first and not last
        memo1 = [0] * (len(nums)-1)
        memo1[0] = nums[0]
        memo1[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            memo1[i] = max(memo1[i-1], memo1[i-2] + nums[i])
        
        max1 = memo1[-1]

        #use last and not first
        memo2 = [0] * len(nums)
        memo2[1] = nums[1]
        memo2[2] = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            memo2[i] = max(memo2[i-1], memo2[i-2] + nums[i])
        max2 = memo2[-1]
        return max(max1, max2)
        