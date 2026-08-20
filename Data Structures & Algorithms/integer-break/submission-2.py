class Solution:
    def integerBreak(self, n: int) -> int:
        answer = [0] * (n+1)
        answer[2] = 1

        for i in range(3, n+1):
            for j in range(i):
                difference = i-j
                answer[i] = max(answer[i], j * difference, answer[difference] * j)
        return answer[n]

                 