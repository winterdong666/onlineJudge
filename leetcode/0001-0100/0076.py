def judge(dic):
    for i in dic.keys():
        if dic[i] > 0:
            return False
    return True

class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        dic = {}
        tmp = []
        for i in t:
            dic[i] = dic.get(i, 0) + 1
        if len(s) < len(t) or t == "":
            return ""
        h, r, count = 0, 0, len(t)
        resLen, res = 2147483647, ""
        if s[r] in dic.keys():
            dic[s[r]] -= 1
            count -= 1
            if judge(dic):
                return t
        r += 1
        while r < len(s):
            if s[r] in dic.keys():
                dic[s[r]] -= 1
                count -= 1
                if judge(dic):
                    while judge(dic):
                        if s[h] in dic.keys():
                            dic[s[h]] += 1
                            count += 1
                        h += 1
                    h -= 1
                    dic[s[h]] -= 1
                    count -= 1
                    if r - h + 1 < resLen:
                        resLen = r - h + 1
                        res = s[h:r + 1]
            r += 1
        return res
            
