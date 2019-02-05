class Solution:
    def fullJustify(self, words: 'List[str]', maxWidth: 'int') -> 'List[str]':
        res = []
        wordLen = []
        for i in words:
            wordLen.append(len(i))
        p = 0
        while p < len(words):
            pre = p
            remain = maxWidth
            while p < len(words) and wordLen[p] <= remain:
                remain -= wordLen[p]
                remain -= 1
                p += 1
            if p < len(words):
                resLine = ""
                space = maxWidth
                wordCount = p - pre
                if wordCount == 1:
                    resLine = resLine + words[pre] + " " * (maxWidth - wordLen[pre])
                else:
                    for i in range(pre, p):
                        space -= wordLen[i]
                    base = space // (wordCount - 1)
                    spaceCount = [base] * (wordCount - 1)
                    tmpSpace = base * (wordCount - 1)
                    t = 0
                    while tmpSpace < space:
                        spaceCount[t] += 1
                        t += 1
                        tmpSpace += 1
                    for i in range(wordCount - 1):
                        resLine = resLine + words[pre + i] + " " * spaceCount[i]
                    resLine = resLine + words[p - 1]
                res.append(resLine)
            else:
                resLine = ""
                for i in range(pre, p):
                    resLine = resLine + words[i]
                    if i != p - 1:
                        resLine = resLine + " "
                l = len(resLine)
                resLine = resLine + " " * (maxWidth - l)
                res.append(resLine)
        return res
