class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i1 = 0
        i2 = n-1
        i = 0
        while i <= i2:
            if nums[i] == 0:
                nums[i1] = 0
                i1 += 1
            elif nums[i] == 2:
                nums[i], nums[i2] = nums[i2], nums[i]
                i2 -= 1
                i -= 1
            i += 1
        while i1 <= i2:
            nums[i1] = 1
            i1 += 1
        