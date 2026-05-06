class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res = -1
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                res = mid
                end = mid-1
            else:
                start = mid+1
        return len(nums) if res == -1 else res