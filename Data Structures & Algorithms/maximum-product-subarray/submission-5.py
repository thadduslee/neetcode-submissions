class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = max(nums)

        maximum = 1
        minimum = 1
        for num in nums:
            if num == 0:
                maximum = 1
                minimum = 1
                continue
            else:
                temp = maximum*num
                maximum = max(temp , num*minimum, num)
                minimum = min(temp, num*minimum, num)
                answer = max(maximum, answer)
        return answer