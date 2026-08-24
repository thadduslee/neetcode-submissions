class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i >= len(nums):
                if subset not in res:
                    res.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtrack(i+1, subset)

            subset.pop()
            backtrack(i+1, subset)
        backtrack(0, [])
        return res