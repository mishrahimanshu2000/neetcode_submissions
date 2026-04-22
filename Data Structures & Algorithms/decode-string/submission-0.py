class Solution:
    def decodeString(self, s: str) -> str:
        sstk = []
        cstk = []
        k = 0
        curr = ''
        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == '[':
                sstk.append(curr)
                cstk.append(k)
                k = 0
                curr = ''
            elif c  == ']':
                temp = sstk.pop()
                cnt = cstk.pop()
                curr = temp + curr * cnt
            else:
                curr += c
            
        return curr