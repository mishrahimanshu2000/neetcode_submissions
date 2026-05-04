class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(open, close, st):
            if open == close == n:
                res.append(str(st))
                return
            if close > open or open > n:
                return
            helper(open+1, close, st+'(')
            helper(open, close+1, st+')')

        helper(0,0,'')
        return res