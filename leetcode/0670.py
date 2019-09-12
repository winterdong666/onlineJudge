class Solution:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        if len(s) == 1:
            return num
        for i in range(1, len(s)):
            if int(s[i]) > int(s[i - 1]):
                for k in range(i + 1, len(s)):
                    if int(s[k]) >= int(s[i]):
                        i = k
                c = 0
                for j in range(0, i):
                    if int(s[i]) > int(s[j]):
                        c = j
                        break
                s = s[:c] + s[i] + s[c + 1: i] + s[c] + s[i + 1:]
                break
        return int(s)
