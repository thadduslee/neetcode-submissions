class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        answer = [0] * (len(cost) + 1)
        for i in range(2, len(cost)+1):
            answer[i] = min(answer[i-2] + cost[i-2], answer[i-1] + cost[i-1])
        return answer[len(cost)]