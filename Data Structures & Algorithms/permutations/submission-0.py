class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(idx, sub, st):
            if len(sub) == len(nums):
                res.append(sub[:])
                return
            if idx >= len(nums):
                return
            backtrack(idx+1, sub, st)
            for i in nums:
                if i not in st:
                    sub.append(i)
                    st.add(i)
                    backtrack(idx+1,sub,st)
                    sub.pop()
                    st.remove(i)
        
        backtrack(0,[],set())
        return res