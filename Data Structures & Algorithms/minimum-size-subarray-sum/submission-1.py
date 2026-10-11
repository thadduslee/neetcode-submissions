class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        length = float('inf')
        count = 0

        while right < len(nums):
            count += nums[right]
            while count >= target and left <= right:
                length = min(length, right-left+1)
                count -= nums[left]
                left+=1
            right+=1
        
        if length == float('inf'):
            return 0
        return length
            
