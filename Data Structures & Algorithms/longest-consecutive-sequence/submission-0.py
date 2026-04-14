class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0
        for num in num_set:
            if num-1 in num_set:
                continue
            cnt = 0
            while num in num_set:
                cnt += 1
                num += 1
            ans = max(cnt, ans)
        return ans