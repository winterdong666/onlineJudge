class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        #return " ".join(words)
        l = len(words)
        valid = [0] * l
        resLen = 0
        resWord = ""
        for i in range(l):
            if len(words[i]) == 1:
                valid[i] = 1
                if resLen < len(words[i]):
                    resLen = len(words[i])
                    resWord = words[i]
            elif i >= 1:
                for j in range(i - 1, -1, -1):
                    if words[j] == words[i][:-1]:
                        if valid[j] == 1:
                            valid[i] = 1
                            if resLen < len(words[i]):
                                resLen = len(words[i])
                                resWord = words[i]
                        break
        return resWord
