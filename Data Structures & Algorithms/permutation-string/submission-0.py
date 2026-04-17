class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        d_s1 = Counter(s1)
        d_s2 = {}
        for r in range(len(s1)):
            d_s2[s2[r]] = d_s2.get(s2[r],0)+1
        if d_s1 == d_s2:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            d_s2[s2[r]] = d_s2.get(s2[r],0)+1
            d_s2[s2[l]] -= 1
            if d_s2[s2[l]] == 0:
                d_s2.pop(s2[l])
            l += 1
            if d_s1 == d_s2:
                return True
        return False