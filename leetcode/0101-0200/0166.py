class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        sign = 1
        if numerator < 0:
            numerator = -numerator
            sign *= -1
        if denominator < 0:
            denominator = -denominator
            sign *= -1
        
        left = numerator // denominator
        newNumerator = numerator % denominator
        if newNumerator == 0:
            if sign == 1:
                return str(left)
            else:
                return "-" + str(left)
        edge = denominator
        countZero = 0
        while edge % 2 == 0:
            edge //= 2
            if newNumerator % 2 != 0:
                newNumerator *= 10
                countZero += 1
            newNumerator //= 2
        while edge % 5 == 0:
            edge //= 5
            if newNumerator % 5 != 0:
                newNumerator *= 10
                countZero += 1
            newNumerator //= 5
        while newNumerator * 10 < edge:
            newNumerator *= 10
            countZero += 1
        rightFirst = newNumerator // edge
        zeros = countZero - len(str(rightFirst))
        newNumerator = newNumerator % edge
        t = rightFirst
        if newNumerator == 0:
            if sign == 1:
                return str(left) + "." + "0" * zeros + str(rightFirst)
            else:
                return "-" + str(left) + "." + "0" * zeros + str(rightFirst)
        origin = newNumerator
        rightSecond = str(newNumerator * 10 // edge)
        newNumerator = newNumerator * 10 % edge
        while newNumerator != origin:
            rightSecond = rightSecond + str(newNumerator * 10 // edge)
            newNumerator = newNumerator * 10 % edge
        if sign == 1:
            if t == 0:
                return str(left) + "." + "0" * (zeros + 1) + "(" + rightSecond + ")"
            else:
                return str(left) + "." + "0" * zeros + str(rightFirst) + "(" + rightSecond + ")"
        else:
            if t == 0:
                return "-" + str(left) + "." + "0" * (zeros + 1) + "(" + rightSecond + ")"
            else:
                return "-" + str(left) + "." + "0" * zeros + str(rightFirst) + "(" + rightSecond + ")"
        
        
