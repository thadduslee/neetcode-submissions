class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        index_trusts_somebody = [False] * n

        index_is_trusted_by_somebody = [0] * n

        for truster, trustee in trust:
            index_trusts_somebody[truster-1] = True
            index_is_trusted_by_somebody[trustee-1] +=1
        
        candidates = []
        for i in range(n):
            if index_trusts_somebody[i] == False:
                candidates.append(i+1)
        
        for candidate in candidates:
            if index_is_trusted_by_somebody[candidate-1] == n-1:
                return candidate
            
        return -1