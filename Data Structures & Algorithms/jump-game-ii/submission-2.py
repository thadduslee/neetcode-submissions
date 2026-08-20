class Solution:
    def jump(self, nums: List[int]) -> int:
        
        def backtrack(i):
            if i >= len(nums)-1:
                return 0
            smallest = float("inf")
            for j in range(1, nums[i]+1):
                smallest = min(smallest,1 + backtrack(j + i))
            return smallest
        return backtrack(0)
        
