class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        bitM, bitN = [], []
        while m != 0:
            bitM.append(m % 2)
            m //= 2
        while n != 0:
            bitN.append(n % 2)
            n //= 2
        while len(bitM) < len(bitN):
            bitM.append(0)
        res = 0
        base = 1
        for i in range(1, len(bitM)):
            base *= 2
        for i in range(len(bitM) - 1, -1, -1):
            if bitM[i] == bitN[i]:
                if bitM[i] == 1:
                    res += base
                base //= 2
            else:
                break
        return res
