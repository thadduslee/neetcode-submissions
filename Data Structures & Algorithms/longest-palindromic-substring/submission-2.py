class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def is_palindrome(string):
            if string == string[::-1]:
                return True
            return False

        longest = 0
        string = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                temp = s[i:j+1]
                if is_palindrome(temp):
                    if len(temp) > longest:
                        longest = len(temp)
                        string = temp
        return string
                
