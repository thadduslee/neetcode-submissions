class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        have, need = 0,len(set(t))
        countT = Counter(t)
        length = float("inf")
        answer = [0,0]
        left = 0
        count = {}
        for right in range(len(s)):
            char = s[right]
            count[char] = 1 + count.get(char,0)
            if char in countT and count[char] == countT[char]:
                have +=1
            while have == need:
                if right-left+1 < length:
                    length = right-left+1
                    answer = [left,right]
                count[s[left]]-=1
                if s[left] in countT and count[s[left]] < countT[s[left]]:
                    have -=1
                left+=1
        left, right = answer
        if length != float("infinity"):
            return s[left:right+1]
        return ""