class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        answer = [0] * (amount +1)

        for i in range(1, amount +1):
            minn = float("inf")
            for coin in coins:
                difference = i- coin
                if difference < 0:
                    continue
                else:
                    minn = min(minn, 1 + answer[difference])
            answer[i] = minn
        if answer[amount] == float("inf"):
            return -1
        return answer[amount]