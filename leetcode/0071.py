class Solution:
    def simplifyPath(self, path: 'str') -> 'str':
        i = 1
        while i < len(path):
            while i < len(path) and path[i] == '/' and path[i - 1] == '/':
                path = path[:i] + path[i + 1:]
            i += 1
        i -= 1
        if path[-1] == '/':
            path = path[:-1]
        path = path[1:]
        ele = path.split('/')
        stack = []
        for i in ele:
            if i == "..":
                if stack != []:
                    stack.pop()
            elif i == ".":
                continue
            else:
                stack.append(i)
        if stack == []:
            return "/"
        res = "/"
        for i in stack:
            res = res + i + "/"
        return res[:-1]
