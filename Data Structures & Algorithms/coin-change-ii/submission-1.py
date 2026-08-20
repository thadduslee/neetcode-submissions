class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = [0] * (amount +1)

        memo[0] = 1
        for coin in coins:
            for i in range(1, amount+1):
                difference = i-coin
                if difference >= 0:
                    memo[i] += memo[difference]
        return memo[amount]