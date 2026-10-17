class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = max(nums)

        minimum = 1
        maximum = 1

        for num in nums:
            temp = num* maximum

            maximum = max(num, temp, num*minimum)
            minimum = min(num, temp, num*minimum)
            answer = max(maximum, answer)
        
        return answer