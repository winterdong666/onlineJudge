class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def changeString(s):
            res = ""
            dic = {}
            pointer = 97
            for i in s:
                if dic.get(i, -1) == -1:
                    dic[i] = chr(pointer)
                    pointer += 1
                    res = res + dic[i]
                else:
                    res = res + dic[i]
            return res
        return changeString(s) == changeString(t)
