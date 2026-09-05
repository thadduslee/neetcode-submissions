class Solution:
    def climbStairs(self, n: int) -> int:
        num = [0] * (n+1)
        num[0] = 1
        num[1] = 1
        for i in range(2, n+1):
            num[i] = num[i-1] + num[i-2]
        return num[n]