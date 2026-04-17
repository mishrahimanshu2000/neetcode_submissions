class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = 0
        max_freq = 0
        ans = 0
        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0)+1
            max_freq = max(max_freq, d[s[r]])
            win_size = r-l+1
            if win_size - max_freq > k:
                d[s[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans