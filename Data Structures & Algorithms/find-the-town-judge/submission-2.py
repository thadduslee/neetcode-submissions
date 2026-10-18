class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts_somebody = [False] * (n+1)
        trusts_somebody[0] = True
        is_trusted = defaultdict(list)

        for truster, gets_trusted in trust:
            trusts_somebody[truster] = True

            is_trusted[gets_trusted].append(truster)
        
        possible = []

        for i in range(n+1):
            if trusts_somebody[i] == False:
                possible.append(i)
        
        for temp in possible:
            if len(is_trusted[temp]) == n-1:
                return temp
        
        return -1


