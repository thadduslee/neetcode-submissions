class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        count = Counter(nums)

        def backtrack():
            if len(subset) == len(nums):
                result.append(subset.copy())
                return
            
            for num in nums:
                if count[num] > 0:
                    count[num] -=1
                    subset.append(num)
                    backtrack()

                    subset.pop()
                    count[num]+=1
        backtrack()
        return result