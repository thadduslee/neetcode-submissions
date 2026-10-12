class Solution:
    def climbStairs(self, n: int) -> int:
        number = [0] * (n+1)
        if n == 0 or n ==1:
            return 1
        
        number[0] = 1

        number[1] = 1

        for i in range(2, n+1):
            number[i] = number[i-1] + number[i-2]
        
        return number[n]