class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(w):
            cnt = 1
            total = 0
            for i in weights:
                total += i
                if total > w:
                    cnt+=1
                    total = i
                if cnt > days:
                    return False
            return cnt <= days
        
        start = max(weights)
        end = sum(weights)
        ans = -1
        while start <= end:
            mid = start + (end-start)//2
            if check(mid):
                ans = mid
                end = mid-1
            else:
                start = mid+1
            
        return ans