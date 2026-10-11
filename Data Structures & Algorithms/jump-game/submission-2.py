class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumpable = [False] * len(nums)
        jumpable[0] = True

        for i in range(len(nums)):
            num = nums[i]
            if not jumpable[i]:
                continue
            for j in range(num+1):
                if i+j < len(nums):
                    jumpable[i+j] = True
        
        return jumpable[-1]