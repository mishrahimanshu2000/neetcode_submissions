class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 1, len(nums)
        while l < r:
            sm = nums[l-1] + nums[r-1]
            if sm == target:
                return [l, r]
            elif sm > target:
                r -= 1
            else:
                l += 1
            
        return []