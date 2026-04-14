class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = []
        left.append(1)
        for i in range(1,n):
            left.append(left[-1]*nums[i-1])
        right = 1
        for i in range(n-1, -1, -1):
            left[i] *= right
            right *= nums[i]
        return left
        