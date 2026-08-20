class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first = target[0]
        second = target[1]
        third = target[2]
        max_a = max_b = max_c = 0
        for a,b,c in triplets:
            if a <= first and b <= second and c<= third:
                max_a = max(max_a, a)
                max_b = max(max_b, b)
                max_c = max(max_c, c)
        return [max_a, max_b, max_c] == target