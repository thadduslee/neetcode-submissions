class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = [0] * 26
        count2 = [0] * 26
        for i in range(len(s1)):
            count1[ord(s1[i])-ord('a')] +=1
            count2[ord(s2[i])-ord('a')] +=1
        matches = 0
        for i in range(len(count1)):
            if count1[i] == count2[i]:
                matches +=1
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            indexright = ord(s2[right]) - ord('a')
            count2[indexright]+=1
            if count2[indexright] == count1[indexright]:
                matches +=1
            elif count2[indexright] -1 == count1[indexright]:
                matches -=1
            
            indexleft = ord(s2[left]) - ord('a')
            count2[indexleft] -=1
            if count2[indexleft] == count1[indexleft]:
                matches +=1
            elif count2[indexleft] + 1 == count1[indexleft]:
                matches -=1
            left +=1
        return matches == 26