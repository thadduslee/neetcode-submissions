class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        res = float('inf')
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                total -= nums[left]
                res = min(res, right - left + 1)
                left +=1
        if res == float('inf'):
            return 0
        return res