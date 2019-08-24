class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        if s == "":
            return count
        c = 0
        if s[c] != " ":
            count += 1
        while c < len(s) - 1:
            if s[c] == " " and s[c + 1] != " ":
                count += 1
            c += 1
        return count
