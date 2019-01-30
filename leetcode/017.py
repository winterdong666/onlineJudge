class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        digitDic = {'2' :["a", "b", "c"],
                   '3' :["d", "e", "f"],
                   '4' :["g", "h", "i"],
                   '5' :["j", "k", "l"],
                   '6' :["m", "n", "o"],
                   '7' :["p", "q", "r", "s"],
                   '8' :["t", "u", "v"],
                   '9' :["w", "x", "y", "z"]}
        if len(digits) == 1:
            return digitDic[digits[0]]
        tmp = self.letterCombinations(digits[1:])
        cur = digitDic[digits[0]]
        res = []
        for i in cur:
            for j in tmp:
                res.append(i + j)
        return res
