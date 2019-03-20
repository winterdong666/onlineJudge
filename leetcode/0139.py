class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        minLen = 2147483647
        words = {}
        for i in wordDict:
            if len(i) < minLen:
                minLen = len(i)
            if words.get(len(i), []) == []:
                words[len(i)] = [i]
            else:
                words[len(i)].append(i)
        DP = [True]
        if len(s) < minLen:
            return False
        for i in range(minLen - 1):
            DP.append(False)
        for i in range(minLen, len(s) + 1):
            find = False
            for j in words.keys():
                if j > i or DP[i - j] == False:
                    continue
                for k in words[j]:
                    if s[i - j: i] == k:
                        find = True
                        break
                if find:
                    break
            if find:
                DP.append(True)
            else:
                DP.append(False)
        return DP[-1]
