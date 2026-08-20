class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        cur = 1
        for i in range(1, n):
            prev, cur = cur, cur + prev
        return cur