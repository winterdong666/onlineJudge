def Match(s, p):
        if s == " " and p == " ":
            return True
        if p == " ":
            return False
        if s == " ":
            if len(p) > 1 and p[1] == '*':
                return Match(s, p[2:])
            return False
        if s[0] != p[0] and p[0] != '.':
            if len(p) > 1 and p[1] == '*':
                return Match(s, p[2:])
            return False
        if len(p) > 2 and p[1] == '*':
            return Match(s[1:], p) or Match(s[1:], p[2:]) or Match(s, p[2:])
        return Match(s[1:], p[1:])

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        for i in range(len(p) - 3):
            if i >= len(p) - 3:
                break
            while (p[i] == p[i + 2] or p[i] == '.') and p[i + 1] == '*' and p[i + 3] == '*':
                p = p[:i + 2] + p[i + 4:]
                if i >= len(p) - 3:
                    break
        s = s + " "
        p = p + " "
        return Match(s, p)
