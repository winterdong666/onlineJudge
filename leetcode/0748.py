class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        plateDic = {}
        for i in licensePlate:
            if i.isalpha():
                t = i.lower()
                plateDic[t] = plateDic.get(t, 0) + 1
        miniLen = 2147483647
        res = ""
        for i in words:
            dic = {}
            for j in i:
                dic[j] = dic.get(j, 0) + 1
            satisfy = True
            for c in plateDic.keys():
                if plateDic[c] > dic.get(c, 0):
                    satisfy = False
                    break
            if satisfy:
                if len(i) < miniLen:
                    res = i
                    miniLen = len(i)
        return res
