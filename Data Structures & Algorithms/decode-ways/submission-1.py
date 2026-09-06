class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        
        answer = [0] * (len(s)+1)
        answer[0] = 1
        answer[1] = 1
        for i in range(2, len(s)+1):
            if s[i-1] != "0":
                answer[i] += answer[i-1]
            
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                answer[i] += answer[i-2]
            
        return answer[len(s)]

        