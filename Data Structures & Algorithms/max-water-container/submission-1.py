class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        left = 0
        right = len(heights)-1

        while left < right:
            height = min(heights[left], heights[right])
            length = right - left
            area = height * length
            maximum = max(maximum, area)

            if heights[left] < heights[right]:
                left+=1
            else:
                right -=1
        return maximum