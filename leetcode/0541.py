class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def helper(s, st, ed):
            t = s[st: ed + 1][::-1]
            s = s[:st] + t + s[ed + 1:]
            return s
        for i in range(0, len(s), 2 * k):
            if i + k > len(s):
                s = helper(s, i, len(s) - 1)
            else:
                s = helper(s, i, i + k - 1)
        return s
