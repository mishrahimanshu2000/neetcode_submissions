class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        def helper(idx, rem, sub):
            if rem == 0:
                ans.append(sub[:])
                return
            if idx >= n or rem < 0:
                return
            for i in range(idx,n):
                sub.append(nums[i])
                helper(i,rem-nums[i],sub)
                sub.pop()
        temp = []
        helper(0,target,temp)
        return ans

