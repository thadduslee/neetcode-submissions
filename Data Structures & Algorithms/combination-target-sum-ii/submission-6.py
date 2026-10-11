class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        subset = []
        candidates.sort()

        def backtrack(i):
            if sum(subset) > target:
                return
            
            if sum(subset) == target:
                results.append(subset.copy())
                return
            if i >= len(candidates):
                return
            
            subset.append(candidates[i])
            backtrack(i+1)

            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i+1)
        
        backtrack(0)
        return results
