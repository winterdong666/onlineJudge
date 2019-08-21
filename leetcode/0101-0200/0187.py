class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        count = {}
        res = []
        for i in range(len(s) - 9):
            tmp = s[i: i + 10]
            count[tmp] = count.get(tmp, 0) + 1
        for i in count.keys():
            if count[i] > 1:
                res.append(i)
        return res
