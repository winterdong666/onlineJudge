class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        while i < len(s) and s[i] == ' ':
            i += 1
        if i == len(s):
            return False
        while s[j] == ' ':
            j -= 1
        s = s[i:j + 1]
        ePosition = -1
        eDigit = False
        digit = ['0','1','2','3','4','5','6','7','8','9']
        for i in range(len(s)):
            if s[i] not in digit and s[i] != 'e' and s[i] != '+' and s[i] != '-' and s[i] != '.':
                return False
            if s[i] == 'e':
                if ePosition != -1 or eDigit == False:
                    return False
                ePosition = i
            if s[i] in digit:
                eDigit = True
        if ePosition != -1:
            s1, s2 = s[:ePosition], s[ePosition + 1:]
            if len(s2) == 0:
                return False
            flag = -1
            hasDigit = False
            for i in range(len(s2)):
                if s2[i] == '.':
                    return False
                if s2[i] == '+' or s2[i] == '-':
                    if i > 0:
                        return False
                if s2[i] in digit:
                    hasDigit = True
            if hasDigit == False:
                return False
            dotPosition = -1
            hasDigit = False
            for i in range(len(s1)):
                if s1[i] == '+' or s1[i] == '-':
                    if i > 0:
                        return False
                if s1[i] == '.':
                    if dotPosition != -1:
                        return False
                    dotPosition = i
                if s1[i] in digit:
                    hasDigit = True
            if s1 == ".":
                return False
            if hasDigit == False:
                return False
        else:
            dotPosition = -1
            hasDigit = False
            for i in range(len(s)):
                if s[i] == '+' or s[i] == '-':
                    if i > 0:
                        return False
                if s[i] == '.':
                    if dotPosition != -1:
                        return False
                    dotPosition = i
                if s[i] in digit:
                    hasDigit = True
            if hasDigit == False:
                return False
            if s == ".":
                return False
        return True
