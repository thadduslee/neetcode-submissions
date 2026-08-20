class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:
        rows, columns = len(nums), len(nums[0])
        leftrow, rightrow = 0, rows - 1
        while leftrow <= rightrow:
            mid = (rightrow-leftrow)//2 + leftrow
            if nums[mid][0] > target:
                rightrow = mid -1
            elif nums[mid][-1] < target:
                leftrow = mid + 1
            else:
                break
        left, right = 0, columns -1
        while left <= right:
            middle = (right-left)//2 + left
            if nums[mid][middle] == target:
                return True
            elif nums[mid][middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return False
