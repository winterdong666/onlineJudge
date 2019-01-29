class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        t = str
        newT = ""
        for i in range(len(t)):
            if t[i] != ' ':
                newT = newT + t[i]
                if i == len(t) - 1 or t[i + 1] == ' ':
                    break
        newDigit = ""
        for i in range(len(newT)):
            if newT[i] == '-' or newT[i] == '+' or (newT[i] >= '0' and newT[i] <= '9'):
                newDigit = newDigit + newT[i]
            else:
                break
            if i == len(newT) - 1 or (newT[i + 1] < '0' or newT[i + 1] > '9'):
                break
        if newDigit == "":
            return 0
        
        positive = True
        if newDigit[0] == '-':
            if len(newDigit) == 1:
                return 0
            positive = False
            newDigit = newDigit[1:]
        if newDigit[0] == '+':
            if len(newDigit) == 1:
                return 0
            newDigit = newDigit[1:]
        res = 0
        for i in range(len(newDigit)):
            res = res * 10 + int(newDigit[i])
            if i == len(newDigit) - 1:
                break
            if positive == True and (res > 214748364 or (res == 214748364 and int(newDigit[i + 1]) > 7)):
                return 2147483647
            if positive == False and (res > 214748364 or (res == 214748364 and int(newDigit[i + 1]) > 7)):
                return -2147483648
        if positive:
            return res
        else:
            return -res
        
