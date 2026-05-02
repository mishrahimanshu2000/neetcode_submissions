class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def helper(idx, sub):
            if idx >= n:
                ans.append(sub[:])
                return
            
            sub.append(nums[idx])
            helper(idx+1,sub)
            sub.pop()
            helper(idx+1,sub)
        helper(0,[])
        return ans