class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        memo = {}
        total = sum(stones)
        target = (sum(stones)+1)//2
        def dfs(i, cur_sum):
            if i == len(stones) or cur_sum >= target:
                return abs(cur_sum - (total -cur_sum))
            
            if (i, cur_sum) in memo:
                return memo[(i,cur_sum)]
            
            memo[(i, cur_sum)] = min(dfs(i+1, cur_sum + stones[i]), dfs(i+1, cur_sum))
            return memo[(i,cur_sum)]
        return dfs(0,0)
            
