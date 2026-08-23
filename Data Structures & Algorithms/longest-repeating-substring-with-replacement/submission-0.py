class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        answer = 0

        left = 0
        maxfreq = 0
        for right in range(len(s)):
            if s[right] not in hashmap:
                hashmap[s[right]] = 0
            hashmap[s[right]] +=1

            maxfreq = max(maxfreq, hashmap[s[right]])

            while (right-left+1) - maxfreq > k:
                hashmap[s[left]] -= 1
                left +=1
            answer = max(answer, right-left+1)
        return answer
