class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        largest_sum = float("-inf")
        for num in nums:
            cur_sum += num
            largest_sum = max(largest_sum, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        return largest_sum