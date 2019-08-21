class Solution:
    def reverseWords(self, s: str) -> str:
        t = s.split(" ")
        i = 0
        while i < len(t):
            if t[i] == '':
                t = t[:i] + t[i + 1:]
            else:
                i += 1
        t = t[::-1]
        return " ".join(t)
