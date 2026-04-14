class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        min_len = min([len(st) for st in strs])
        ans = 0
        for i in range(min_len):
            for j in range(1, n):
                if strs[j][i] != strs[j-1][i]:
                    return strs[j][:ans]
            ans += 1
        return strs[0][:ans]