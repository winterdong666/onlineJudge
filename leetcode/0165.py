class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ls1, ls2 = version1.split("."), version2.split(".")
        while len(ls1) < len(ls2):
            ls1.append(0)
        while len(ls2) < len(ls1):
            ls2.append(0)
        for t in range(len(ls1)):
            i = ls1[t]
            j = ls2[t]
            if int(i) < int(j):
                return -1
            elif int(i) > int(j):
                return 1
            else:
                continue
        return 0
