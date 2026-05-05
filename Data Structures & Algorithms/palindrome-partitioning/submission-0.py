class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        def isPalindrom(st):
            start = 0 
            end = len(st)-1
            while start <= end:
                if st[start] != st[end]:
                    return False
                start+=1
                end-=1
            return True
        
        def helper(s, sub):
            if not s or len(s) == 0:
                res.append(sub[:])
                return
            for i in range(1,len(s)+1):
                cut = s[:i]
                if not isPalindrom(cut):
                    continue
                sub.append(cut)
                helper(s[i:], sub)
                sub.pop()
        
        helper(s,[])
        return res