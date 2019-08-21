class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        stack = []
        res = 0
        pos = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) > 0:
                    stack.pop()
                else:
                    res = max(res, i - pos)
                    pos = i + 1
        for i in range(len(stack) - 1):
            res = max(res, stack[i + 1] - stack[i] - 1)
        if len(stack) > 0:
            res = max(res, stack[0] - pos)
            res = max(res, len(s) - stack[-1] - 1)
        else:
            res = max(res, len(s) - pos)
        return res
