class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []
        def helper(idx, target, sub):
            if target == 0:
                res.append(sub[:])
                return
            if idx >= n or target < 0:
                return
            sub.append(candidates[idx])
            helper(idx+1,target-candidates[idx],sub)
            sub.pop()
            while idx < n-1 and candidates[idx] == candidates[idx+1]:
                idx+=1
            helper(idx+1,target,sub) 
        helper(0,target,[])
        return res