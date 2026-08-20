class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:
        for i in range(len(nums)):
            if target in nums[i]:
                return True
        return False