class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        elif num == 1:
            return True
        flag = True
        while flag and (num != 2 and num != 3 and num != 5):
            flag = False
            if num % 2 == 0:
                num //= 2
                flag = True
            elif num % 3 == 0:
                num //= 3
                flag = True
            elif num % 5 == 0:
                num //= 5
                flag = True
        return flag
