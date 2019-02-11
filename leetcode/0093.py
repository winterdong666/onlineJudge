class Solution:
    def restoreIpAddresses(self, s: 'str') -> 'List[str]':
        def restoreHelper(s, remain):
            if s == "":
                return []
            if len(s) > remain * 3:
                return []
            if remain == 1:
                if int(s) <= 255 and ((int(s) == 0 and len(s) == 1) or s[0] != "0"):
                    return [s]
                else:
                    return []
            res = []
            if s[0] == "0":
                res1 = restoreHelper(s[1:], remain - 1)
                for i in res1:
                    if remain > 1:
                        tmp = s[:1] + "." + i
                    else:
                        tmp = s[:1] + i
                    res.append(tmp)
                return res
            res1, res2, res3 = [], [], []
            if len(s) >= remain:
                res1 = restoreHelper(s[1:], remain - 1)
                for i in res1:
                    if remain > 1:
                        tmp = s[:1] + "." + i
                    else:
                        tmp = s[:1] + i
                    res.append(tmp)
                if len(s) >= remain + 1:
                    res2 = restoreHelper(s[2:], remain - 1)
                    for i in res2:
                        if remain >= 1:
                            tmp = s[:2] + "." + i
                        else:
                            tmp = s[:2] + i
                        res.append(tmp)
                    if len(s) >= remain + 2 and int(s[:3]) <= 255:
                        res3 = restoreHelper(s[3:], remain - 1)
                        for i in res3:
                            if remain > 1:
                                tmp = s[:3] + "." + i
                            else:
                                tmp = s[:3] + i
                            res.append(tmp)
            return res
        return restoreHelper(s, 4)
