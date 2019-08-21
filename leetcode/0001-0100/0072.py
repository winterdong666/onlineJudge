class Solution:
    def minDistance(self, word1: 'str', word2: 'str') -> 'int':
        word1 = word1[::-1]
        word2 = word2[::-1]
        if word1 == "" and word2 == "":
            return 0
        if word1 == "":
            return len(word2)
        if word2 == "":
            return len(word1)
        DP = []
        for i in range(len(word1) + 1):
            tmp = []
            for j in range(len(word2) + 1):
                tmp.append(0)
            DP.append(tmp)
        
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0:
                    DP[i][j] = j
                else:
                    if j == 0:
                        DP[i][j] = i
                    else:
                        if word1[i - 1] == word2[j - 1]:
                            DP[i][j] = DP[i - 1][j - 1]
                        else:
                            DP[i][j] = min(DP[i - 1][j], DP[i][j - 1], DP[i - 1][j - 1]) + 1
        return DP[-1][-1]
