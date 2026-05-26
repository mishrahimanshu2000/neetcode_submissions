class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        o = {}
        for i,ch in enumerate(order):
            o[ch] = i
        for i in range(1,len(words)):
            a = words[i-1]
            b = words[i]
            for j in range(len(a)):
                if j == len(b):
                    return False
                ca = a[j]
                cb = b[j]
                if o[ca] < o[cb]:
                    break
                if o[ca] > o[cb]:
                    return False
        return True