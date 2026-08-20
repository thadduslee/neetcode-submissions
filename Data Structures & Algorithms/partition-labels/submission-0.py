class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        for i in range(len(s)):
            char = s[i]
            hashmap[char] = i
        answer =[]
        
        count = 0
        end = 0
        for index, value in enumerate(s):
            count +=1
            end = max(end, hashmap[value])

            if index == end:
                answer.append(count)
                count = 0
        return answer
        