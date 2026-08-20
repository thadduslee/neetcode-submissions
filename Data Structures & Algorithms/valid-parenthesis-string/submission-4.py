class Solution:
    def checkValidString(self, s: str) -> bool:
        openmin = 0
        openmax = 0
        for char in s:
            if char == "(":
                openmin +=1
                openmax +=1
            elif char == "*":
                openmin -=1
                openmax +=1
            elif char == ")":
                if openmax == 0:
                    return False
                openmin -=1
                openmax -=1
            if openmin < 0:
                openmin = 0
        return openmin == 0