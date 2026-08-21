class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        for character in s:
            if character.isalnum():
                temp.append(character.lower())
        temp = ''.join(temp)
        first = 0
        last = len(temp)-1
        while first < last:
            if temp[first] != temp[last]:
                return False
            first +=1
            last -=1
        return True