class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        
        start = 1
        end = x//2
        while start <= end:
            mid = start + (end-start)//2
            if mid*mid <= x:
                start = mid+1
            else:
                end = mid-1
        return end
