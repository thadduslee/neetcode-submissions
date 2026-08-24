class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        
        def backtrack(i, combination, length):
            if length == k:
                results.append(combination.copy())
                return

            if length > k or i > n:
                return
            
            
            combination.append(i)
            backtrack(i+1, combination, len(combination))

            combination.pop()
            backtrack(i+1, combination, len(combination))
        
        backtrack(1, [], 0)

        return results