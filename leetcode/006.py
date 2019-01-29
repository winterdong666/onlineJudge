class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        resArray = []
        for i in range(numRows):
            resArray.append([])
        
        x = 0
        up = False
        for i in range(len(s)):
            resArray[x].append(s[i])
            if up == False:
                x += 1
                if x == numRows - 1:
                    up = True
            else:
                for j in range(numRows):
                    if j != x:
                        resArray[j].append(' ')
                x -= 1
                if x == 0:
                    up = False
        res = ""
        for i in range(numRows):
            for j in resArray[i]:
                if j != ' ':
                    res = res + j
        return res
                
