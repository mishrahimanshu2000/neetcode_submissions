class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        start = 0 
        end = len(s)-1
        while start < end:
            if s[start] != s[end]:
                return isPalindrome(start+1,end) or isPalindrome(start, end-1)
            start += 1
            end -= 1
        return True