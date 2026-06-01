class Solution:
    def climbStairs(self, n: int) -> int:
        last = 1
        s_last = 1
        for i in range(n-1):
            s_last, last = last, s_last + last
        return last