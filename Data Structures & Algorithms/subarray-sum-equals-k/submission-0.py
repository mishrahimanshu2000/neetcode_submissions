class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen_sum = {0:1}
        sm = 0
        ans = 0
        for num in nums:
            sm += num
            ans += seen_sum.get(sm-k,0)
            seen_sum[sm] = seen_sum.get(sm, 0)+1
        return ans