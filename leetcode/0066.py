class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = digits[::-1]
        res[0] += 1
        i = 1
        jinwei = res[0] // 10
        res[0] %= 10
        while jinwei and i < len(res):
            res[i] += jinwei
            jinwei = res[i] // 10
            res[i] %= 10
            i += 1
        if jinwei:
            res.append(1)
        return res[::-1]
            
