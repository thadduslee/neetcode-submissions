class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        for index, value in enumerate(s):
            hashmap[value] = index
        
        count = 0
        end = 0
        answer = []
        for index, value in enumerate(s):
            count +=1
            end = max(end, hashmap[value])
            if index == end:
                answer.append(count)
                count = 0
        return answer