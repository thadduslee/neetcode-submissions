class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        hashmap = {}
        count = 0 

        while right < len(s):
            while left <= right and s[right] in hashmap:
                del hashmap[s[left]]
                left+=1
            else:
                hashmap[s[right]] = 1
            count = max(count,len(hashmap))
            right +=1
        return count
