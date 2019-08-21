class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = a[::-1], b[::-1]
        i = 0
        jinwei = 0
        res = ""
        while i < len(a) and i < len(b):
            tmp = jinwei + int(a[i]) + int(b[i])
            res = res + str(tmp % 2)
            jinwei = tmp // 2
            i += 1
        while i < len(a):
            tmp = jinwei + int(a[i])
            res = res + str(tmp % 2)
            jinwei = tmp // 2
            i += 1
        while i < len(b):
            tmp = jinwei + int(b[i])
            res = res + str(tmp % 2)
            jinwei = tmp // 2
            i += 1
        if jinwei == 1:
            res = res + "1"
        return res[::-1]
