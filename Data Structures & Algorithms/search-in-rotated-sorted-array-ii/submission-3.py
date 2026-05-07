class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                return True
            elif nums[mid] == nums[start] == nums[end]:
                start += 1
                end -= 1
            elif nums[start] <= nums[mid]:
                # start - mid is sorted
                if nums[start] <= target and nums[mid] > target:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if nums[mid] < target and nums[end] >= target:
                    start = mid+1
                else:
                    end = mid-1
        return False
