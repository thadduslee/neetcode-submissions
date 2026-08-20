class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        count = Counter(nums)
        def backtrack():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for num in nums:
                if count[num] > 0:
                    sol.append(num)
                    count[num]-=1
                    backtrack()
                    sol.pop()
                    count[num]+=1
        backtrack()
        return res
            