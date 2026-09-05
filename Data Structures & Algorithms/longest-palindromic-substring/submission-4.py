class Solution:
    def longestPalindrome(self, s: str) -> str:
        index = 0
        length = 0
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if(right-left+1) > length:
                    length = right-left+1
                    index = left
                
                left -=1
                right +=1
            
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if(right-left+1) > length:
                    length = right-left+1
                    index = left
                
                left -=1
                right +=1
        return s[index: index + length]
            

