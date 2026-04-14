class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for st in strs:
            key = sorted(st)
            groups[str(key)].append(st)
        return list(groups.values())