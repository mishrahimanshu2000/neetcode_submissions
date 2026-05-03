class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def helper(idx, sub):
            res.append(sub[:])
            for i in range(idx,len(nums)):
                if i != idx and nums[i] == nums[i-1]:
                    continue
                sub.append(nums[i])
                helper(i+1,sub)
                sub.pop()
        
        helper(0,[])
        return res