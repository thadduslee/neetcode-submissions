class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_cost = [0] * (len(cost)+1)
        for i in range(2,len(cost)+1):
            total_cost[i] = min(total_cost[i-2]+cost[i-2], total_cost[i-1] + cost[i-1])
        
        return total_cost[len(cost)]