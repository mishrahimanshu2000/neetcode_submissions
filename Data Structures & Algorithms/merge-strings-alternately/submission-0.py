class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = []
        i1 = i2 = 0
        w1_len, w2_len = len(word1), len(word2)
        while i1 < w1_len and i2 < w2_len:
            word.append(word1[i1])
            word.append(word2[i2])
            i1 += 1
            i2 += 1
        word.append(word1[i1:w1_len])
        word.append(word2[i2:w2_len])
        return ''.join(word)