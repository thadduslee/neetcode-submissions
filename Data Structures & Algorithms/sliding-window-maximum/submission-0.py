class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        answer = [0] * (len(nums)-k+1)
        right = k-1
        window = []
        currentmax = 0
        for i in range(left,right+1):
            window.append(nums[i])
        currentmax = max(window)
        answer[left] = currentmax
        for right in range(k, len(nums)):
            window.append(nums[right])
            window.remove(nums[left])
            currentmax  = max(window)
            left+=1
            answer[left] = currentmax
        return answer