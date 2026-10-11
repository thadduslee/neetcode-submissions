class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        subsets = []

        def backtrack(i):
            if len(subsets) == k:
                results.append(subsets.copy())
                return
            
            if i > n:
                return
            
            subsets.append(i)
            backtrack(i+1)

            subsets.pop()
            backtrack(i+1)
        
        backtrack(1)
        return results
