class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) < len(needle):
            return -1
        if needle == "":
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            find = False
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    find = False
                    break
                find = True
            if find:
                return i
        return -1
