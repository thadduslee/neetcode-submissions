class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        x = 0
        y = 0

        while x < len(word1) and y< len(word2):
            answer += word1[x]
            answer += word2[y]
            x+=1
            y+=1
        
        while x < len(word1):
            answer += word1[x]
            x+=1
        
        while y < len(word2):
            answer += word2[y]
            y+=1
        return answer