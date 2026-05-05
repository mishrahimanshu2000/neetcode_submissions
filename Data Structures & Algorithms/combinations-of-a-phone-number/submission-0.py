class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        res = []
        if n == 0:
            return res
        d = {
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z']
        }
        def helper(idx,s):
            if idx == n:
                res.append(str(s))
                return
            for ch in d[digits[idx]]:
                helper(idx+1, s+ch)
        helper(0,'')
        return res