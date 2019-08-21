def judge(strs, i):
    s = strs[0][:i]
    for j in strs:
        if s != j[:i]:
            return False
    return True

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        m = len(strs[0])
        for i in strs:
            if len(i) < m:
                m = len(i)
        l, r, res = 0, m, 0
        mid = (l + r) // 2
        while l < r:
            if judge(strs, mid) == False:
                r = mid - 1
            else:
                res = mid
                l = mid + 1
            mid = (l + r) //2
        if l == r:
            if judge(strs, l):
                res = l
        return strs[0][:res]
