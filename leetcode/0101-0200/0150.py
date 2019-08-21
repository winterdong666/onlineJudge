class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(t1 + t2)
            elif i == "-":
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(t2 - t1)
            elif i == "*":
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(t2 * t1)
            elif i == "/":
                t1 = stack.pop()
                t2 = stack.pop()
                if t2 == 0:
                    stack.append(0)
                else:
                    stack.append(abs(t2) // abs(t1) * (t2 // abs(t2)) * (t1 // abs(t1)))
            else:
                stack.append(int(i))
        return stack.pop()
