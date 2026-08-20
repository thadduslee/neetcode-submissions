class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 ==1:
            return False
        target = sum(nums)/2
        def backtrack(i, cur_sum):
            if i == len(nums):
                return False
            if cur_sum == target:
                return True
            
            return backtrack(i+1, cur_sum + nums[i]) or backtrack(i+1, cur_sum)

        return backtrack(0,0)
