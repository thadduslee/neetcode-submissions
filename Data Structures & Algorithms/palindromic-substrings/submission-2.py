class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = 0
        for centre in range(len(s)):
            #odd length palindromes
            left = centre
            right = centre
            while left >= 0 and right < len(s) and s[left] == s[right]:
                answer +=1
                left -=1
                right +=1
            
        for centre in range(len(s)-1):
            left = centre
            right = centre+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                answer +=1
                left -=1
                right +=1
             
        
        return answer
