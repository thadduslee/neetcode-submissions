class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hashmap1 = {}
        for character in s1:
            if character not in hashmap1:
                hashmap1[character] = 0
            hashmap1[character] +=1
        
        left = 0
        right = len(s1)-1
        hashmap2 = {}
        for i in range(left, right+1):
            if s2[i] not in hashmap2:
                hashmap2[s2[i]] = 0
            hashmap2[s2[i]] +=1
        
        if hashmap2 == hashmap1:
            return True
        
        right +=1
        while right < len(s2):
            if s2[right] not in hashmap2:
                hashmap2[s2[right]] = 0
            hashmap2[s2[right]] +=1
            hashmap2[s2[left]] -=1
            if hashmap2[s2[left]] == 0:
                del hashmap2[s2[left]]
            if hashmap2 == hashmap1:
                return True
            right +=1
            left +=1
        
        return False
            
