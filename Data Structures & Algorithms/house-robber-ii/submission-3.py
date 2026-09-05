class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        maximum = [0] * (len(nums)+1)
        maximum[0] = nums[0]
        maximum[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            maximum[i] = max(maximum[i-2] + nums[i], maximum[i-1])
        
        maximum2 = [0] * (len(nums)+1)
        maximum2[1] = nums[1]
        maximum2[2] = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            maximum2[i] = max(maximum2[i-2] + nums[i], maximum2[i-1])

        max1 = max(maximum)
        max2 = max(maximum2)
        return max(max1,max2)