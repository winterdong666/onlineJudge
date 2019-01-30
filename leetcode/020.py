class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif i == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
                stack.pop()
            elif i == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    return False
                stack.pop()
            elif i == '}':
                if len(stack) == 0 or stack[-1] != '{':
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False
