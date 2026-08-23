class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        minimum = 0
        left = 0
        right = len(people)-1
        while left <= right:
            remain = limit - people[right]
            right -=1
            minimum +=1
            if left <= right and remain >= people[left]:
                left +=1
        return minimum
                