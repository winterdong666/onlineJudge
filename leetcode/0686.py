class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        la, lb = len(A), len(B)
        if la >= lb:
            if B in A:
                return 1
            else:
                A = A + A
                if B in A:
                    return 2
                else:
                    return -1
        else:
            if lb % la == 0:
                t = lb // la
            else:
                t = lb // la + 1
            tA = A * t
            if B in tA:
                return t
            else:
                tA = tA + A
                if B in tA:
                    return t + 1
                else:
                    return -1
