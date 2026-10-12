class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        answer = 0
        total_sum = 0
        for i in range(len(gas)):
            total_sum += gas[i] - cost[i]
            if total_sum < 0:
                total_sum = 0
                answer = i+1
        
        return answer