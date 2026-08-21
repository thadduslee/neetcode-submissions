class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapS = {}
        hashmapT = {}
        for character in s:
            if character not in hashmapS:
                hashmapS[character] = 0
            hashmapS[character] +=1
        
        for character in t:
            if character not in hashmapT:
                hashmapT[character] = 0
            hashmapT[character] +=1
        
        for key,value in hashmapS.items():
            if key not in hashmapT:
                return False
            if value != hashmapT[key]:
                return False

        for key,value in hashmapT.items():
            if key not in hashmapS:
                return False
            if value != hashmapS[key]:
                return False
        return True