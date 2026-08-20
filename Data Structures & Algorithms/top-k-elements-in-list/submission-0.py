class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] +=1
            else:
                counter[num] = 1
        frequent = []
        sorted_data = sorted(counter.items(), key = lambda item: item[1], reverse = True)

        for i in range(k):
            frequent.append(sorted_data[i][0])
        return frequent
