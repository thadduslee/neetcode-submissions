class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def backtrack(i):
            if i >= len(nums)-1:
                return 0
            if i in memo:
                return memo[i]
            smallest = float("inf")
            for j in range(1, nums[i]+1):
                smallest = min(smallest,1 + backtrack(j + i))
            memo[i] = smallest
            return memo[i]
        return backtrack(0)
        
