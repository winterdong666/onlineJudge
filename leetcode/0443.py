class Solution:
    def compress(self, chars: List[str]) -> int:
        res = ""
        current = chars[0]
        count = 1
        if len(chars) <= 1:
            return len(chars)
        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                count += 1
            else:
                if count != 1:
                    res = res + chars[i - 1] + str(count)
                else:
                    res = res + chars[i - 1]
                current = chars[i]
                count = 1
        if count != 1:
            res = res + chars[-1] + str(count)
        else:
            res = res + chars[-1]
        for i in range(len(res)):
            chars[i] = res[i]
        return len(res)
