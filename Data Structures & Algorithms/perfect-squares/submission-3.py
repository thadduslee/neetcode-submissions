class Solution:
    def numSquares(self, n: int) -> int:
        answer = [float("inf")] * (n+1)
        answer[0] = 0

        squares = []
        i = 1
        while i * i <= n:
            squares.append(i*i)
            i+=1
        
        for i in range(len(answer)):
            for square in squares:
                if i - square >= 0:
                    answer[i] = min(answer[i], 1 + answer[i-square])
        return answer[n]