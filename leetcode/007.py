class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == -2147483648:
            return 0
        positive = True
        if x < 0:
            positive = False
            x = -x
        
        strx = ""
        while x != 0:
            strx = strx + str(x % 10)
            x = x // 10
        
        res = 0
        for i in range(len(strx)):
            if res > 214748364 or (res == 214748364 and int(strx[i]) >= 8):
                return 0
            res = res * 10 + int(strx[i])
        
        if positive == False:
            res = -res
        
        return res
