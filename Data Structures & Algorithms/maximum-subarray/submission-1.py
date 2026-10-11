class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        largest = float("-inf")

        for num in nums:
            cur_sum +=num

            largest = max(largest, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        
        return largest