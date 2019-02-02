class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        l1 = len(num1)
        l2 = len(num2)
        res = [0] * (l1 + l2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        for i in range(l1):
            for j in range(l2):
                tmp = int(num1[i]) * int(num2[j])
                res[i + j] += tmp
        resStr = ""
        for i in range(l1 + l2 - 1):
            jinwei = res[i] // 10
            res[i] %= 10
            res[i + 1] += jinwei
            resStr = str(res[i]) + resStr
        resStr = str(res[-1]) + resStr
        i = 0
        while resStr[i] == '0':
            i += 1
        return resStr[i:]
        
        
