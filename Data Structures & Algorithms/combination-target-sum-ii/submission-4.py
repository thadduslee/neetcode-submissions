class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        candidates.sort()

        def backtrack(start, cur_sum):
            if target == cur_sum:
                res.append(sol[:])
                return 
            if start == len(candidates) or cur_sum > target:
                return 
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                if cur_sum + candidates[i] > target:
                    break
                
                sol.append(candidates[i])
                backtrack(i+1, cur_sum + candidates[i])
                sol.pop()
        
        backtrack(0,0)
        return res
                

                
