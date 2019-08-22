class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        if num[0] == "0":
            a = 0
            grandA = a
            if num[1] == "0":
                for i in num:
                    if i != "0":
                        return False
            else:
                for i in range(1, len(num) - 1):
                    b = int(num[1: i + 1])
                    c = grandA + b
                    flag = True
                    end = len(str(c)) + i
                    while end < len(num) - 1:
                        if str(c) != num[end + 1 - len(str(c)): end + 1]:
                            flag = False
                            break
                        else:
                            a, b = b, c
                            c = a + b
                            end = len(str(c)) + end
                    if flag == False:
                        continue
                    if end != len(num) - 1:
                        continue
                    if str(c) != num[end + 1 - len(str(c)): end + 1]:
                        continue
                    return True
                return False
        for i in range((len(num) - 1) // 2):
            a = int(num[0: i + 1])
            grandA = a
            if num[i + 1] == "0":
                b = 0
                c = grandA + b
                flag = True
                end = len(str(c)) + i + 1
                while end < len(num) - 1:
                    if str(c) != num[end + 1 - len(str(c)): end + 1]:
                        flag = False
                        break
                    else:
                        a, b = b, c
                        c = a + b
                        end = len(str(c)) + end
                if flag == False:
                    continue
                if end != len(num) - 1:
                    continue
                if str(c) != num[end + 1 - len(str(c)): end + 1]:
                    continue
                return True
            else:
                for j in range(i + 1, len(num) - i):
                    b = int(num[i + 1: j + 1])
                    c = grandA + b
                    flag = True
                    end = len(str(c)) + j
                    while end < len(num) - 1:
                        if str(c) != num[end + 1 - len(str(c)): end + 1]:
                            flag = False
                            break
                        else:
                            a, b = b, c
                            c = a + b
                            end = len(str(c)) + end
                    if flag == False:
                        continue
                    if end != len(num) - 1:
                        continue
                    if str(c) != num[end + 1 - len(str(c)): end + 1]:
                        continue
                    return True
        return False
