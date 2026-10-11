class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        curr_max = 0
        curr_min = 0
        max_sum = nums[0]
        min_sum = nums[0]

        for num in nums:
            total += num
            curr_max = max(curr_max + num, num)
            max_sum = max(curr_max, max_sum)

            curr_min = min(curr_min + num, num)
            min_sum = min(curr_min, min_sum)
        
        if max_sum < 0:
            return max_sum
        
        return max(max_sum, total-min_sum)


