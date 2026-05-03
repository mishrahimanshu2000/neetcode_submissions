class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []
        def helper(idx, target, sub):
            if target == 0:
                res.append(sub[:])
            if idx >= n or target < 0:
                return
            for i in range(idx,n):
                if candidates[i] > target:
                    break
                if i == idx or candidates[i] > candidates[i-1]:
                    sub.append(candidates[i])
                    helper(i+1, target-candidates[i], sub)
                    sub.pop()
        helper(0,target,[])
        return res