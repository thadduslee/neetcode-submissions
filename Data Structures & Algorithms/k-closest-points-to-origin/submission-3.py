class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x,y in points:
            distance = -math.sqrt((x*x)+(y*y))
            heapq.heappush(maxHeap, [distance,x,y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []
        while maxHeap:
            dist,x,y = heapq.heappop(maxHeap)
            res.append([x,y])
        return res