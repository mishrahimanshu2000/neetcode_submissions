class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        res = []
        if n == 0:
            return res
        d = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        def helper(idx,s):
            if idx == n:
                res.append(str(s))
                return
            for ch in d[digits[idx]]:
                helper(idx+1, s+ch)
        helper(0,'')
        return res