class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        left = 0
        right = 0
        maximum = 0
        while right < len(s):
            while s[right] in hashmap:
                del hashmap[s[left]]
                left +=1
            hashmap[s[right]] = 1
            right +=1
            maximum = max(maximum, right - left)
        return maximum
            