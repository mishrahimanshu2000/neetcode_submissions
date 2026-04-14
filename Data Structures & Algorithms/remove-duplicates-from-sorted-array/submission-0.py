class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        idx = 0
        for i in range(1,n):
            if nums[i] != nums[idx]:
                nums[idx+1] = nums[i]
                idx+=1
        return idx+1