class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        subsets = []
        count = Counter(nums)

        def backtrack():
            if len(subsets) == len(nums):
                results.append(subsets.copy())
                return
            
            for num in count:
                if count[num] > 0:
                    subsets.append(num)
                    count[num] -=1
                    backtrack()
                    subsets.pop()
                    count[num]+=1
            
        backtrack()
        
        return results
    
