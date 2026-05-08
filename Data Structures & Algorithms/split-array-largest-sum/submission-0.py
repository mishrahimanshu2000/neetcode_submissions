class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(sm):
            curr_sum = 0
            div = 1
            for num in nums:
                curr_sum += num
                if curr_sum > sm:
                    div+=1
                    curr_sum = num
                if div > k:
                    return False
            return div <= k
        
        mini = max(nums)
        maxi = sum(nums)
        ans = 0 
        while mini <= maxi:
            mid = mini + (maxi-mini)//2
            if check(mid):
                ans = mid
                maxi = mid-1
            else:
                mini = mid+1
        return ans