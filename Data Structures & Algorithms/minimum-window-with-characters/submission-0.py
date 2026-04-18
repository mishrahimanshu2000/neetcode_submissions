class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        freq_t = Counter(t)
        need = len(freq_t)

        win = {}
        have = 0

        ans = float('inf'), None, None
        l = 0
        for r in range(len(s)):
            char = s[r]
            win[char] = win.get(char,0)+1
            if char in freq_t and freq_t[char] == win[char]:
                have += 1
            
            while have == need:
                if r-l+1 < ans[0]:
                    ans = (r-l+1, l, r+1)
                left = s[l]
                win[left] -= 1
                if left in freq_t and freq_t[left] > win[left]:
                    have -= 1
                l += 1
        return '' if ans[0] == float('inf') else s[ans[1]:ans[2]]