class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
        
        answer = []
        for key,value in hashmap.items():
            answer.append(key)
        for i in range(len(answer)):
            nums[i] = answer[i]
        return len(answer)
        
        