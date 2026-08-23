class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        
        for left in range(len(s2)-len(s1)+1):
            word = s2[left: left + len(s1)]
            if sorted(word) == s1:
                return True
        return False
            

