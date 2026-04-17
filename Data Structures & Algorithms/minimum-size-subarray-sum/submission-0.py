class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n+1
        l = 0 
        sm = 0
        for r in range(n):
            sm += nums[r]
            while sm >= target:
                ans = min(ans, r-l+1)
                sm -= nums[l]
                l += 1
        return 0 if ans == n+1 else ans