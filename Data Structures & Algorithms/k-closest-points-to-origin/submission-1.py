class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for x,y in points:
            distance = math.sqrt((x*x)+(y*y))
            distances.append([distance, x,y])
        heapq.heapify(distances)
        res = []
        while k > 0:
            dist,x,y = heapq.heappop(distances)
            res.append([x,y])
            k-=1
        return res