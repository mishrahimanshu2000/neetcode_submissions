class Solution:

    def encode(self, strs: List[str]) -> str:
        s = []
        for st in strs:
            n = len(st)
            s.append(str(n)+'#'+st)
        return ''.join(s)

    def decode(self, s: str) -> List[str]:
        idx = 0
        ans = []
        while idx < len(s):
            n = ''
            while s[idx] != '#':
                n += s[idx]
                idx += 1
            idx += 1 
            n = int(n)
            ans.append(s[idx:idx+n])
            idx += n
        return ans                