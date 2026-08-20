class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:
        rows, columns = len(nums), len(nums[0])
        l, r = 0, rows*columns -1
        while l<=r:
            mid = (r-l)//2+l
            row, column = mid//columns, mid%columns
            if nums[row][column] == target:
                return True
            elif nums[row][column] > target:
                r = mid-1
            elif nums[row][column] < target:
                l = mid + 1
        return False