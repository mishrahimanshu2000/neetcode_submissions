class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isPossible(k):
            time = 0
            for i in piles:
                time += i // k
                if i % k != 0:
                    time += 1
                if time > h:
                    return False
            return time <= h
        
        mini = 1
        maxi = sum(piles)
        while mini <= maxi:
            m = mini + (maxi-mini)//2
            if isPossible(m):
                maxi = m-1
            else:
                mini = m+1
        return mini
