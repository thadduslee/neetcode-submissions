class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        subset = []
        count = Counter(nums)

        def backtrack():
            if len(subset) == len(nums):
                results.append(subset.copy())
                return
            
            for num in nums:
                if count[num] > 0:
                    subset.append(num)
                    count[num] -=1
                    backtrack()
                    subset.pop()
                    count[num]+=1
            
        backtrack()
        return results