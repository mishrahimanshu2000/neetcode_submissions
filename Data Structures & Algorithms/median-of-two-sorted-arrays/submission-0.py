class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        i1 = 0
        i2 = 0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums2[i2] < nums1[i1]:
                nums.append(nums2[i2])
                i2 += 1
            else:
                nums.append(nums1[i1])
                i1 += 1
        nums.extend(nums1[i1:len(nums1)])
        nums.extend(nums2[i2:len(nums2)])

        if len(nums) % 2 == 1:
            return nums[len(nums)//2]
        else:
            i = len(nums)//2
            return (nums[i] + nums[i-1])/2