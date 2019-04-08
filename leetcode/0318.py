class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        l = len(words)
        base = ord('a')
        for i in range(l):
            wordBank = [0] * 26
            for c in words[i]:
                wordBank[ord(c) - base] = 1
            for j in range(i + 1, l):
                match = True
                for c in words[j]:
                    if wordBank[ord(c) - base]:
                        match = False
                        break
                if match:
                    res = max(res, len(words[i]) * len(words[j]))
        return res
