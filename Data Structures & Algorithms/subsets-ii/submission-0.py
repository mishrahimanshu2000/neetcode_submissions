class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def helper(idx, sub):
            if idx == len(nums):
                res.append(sub[:])
                return
            sub.append(nums[idx])
            helper(idx+1,sub)
            sub.pop()
            while idx+1 < len(nums) and nums[idx] == nums[idx+1]:
                idx+=1
            helper(idx+1,sub)
        
        helper(0,[])
        return res