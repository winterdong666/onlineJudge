class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic1, dic2 = {}, {}
        for i in s:
            dic1[i] = dic1.get(i, 0) + 1
        for j in t:
            dic2[j] = dic2.get(j, 0) + 1
        for i in dic2.keys():
            if dic2[i] != dic1.get(i, 0):
                return i
