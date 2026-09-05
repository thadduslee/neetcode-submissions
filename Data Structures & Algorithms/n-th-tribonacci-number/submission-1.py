class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        value = [0] * (n+1)
        value[1] = 1
        value[2] = 1
        for i in range(3,n+1):
            value[i] = value[i-1] + value[i-2] + value[i-3]
        return value[n]