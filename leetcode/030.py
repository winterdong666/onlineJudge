class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if s == "" or words == []:
            return []
        dic = {}
        cnt = len(words)
        res = []
        
        for i in words:
            dic[i] = dic.get(i, 0) + 1
        
        wl = len(words[0])
        
        for i in range(wl):
            count = 0
            head = i
            Tdic = {}
            for j in dic.keys():
                Tdic[j] = 0
            for j in range(i, len(s) - wl + 1, wl):
                if s[j:j + wl] in Tdic:
                    Tdic[s[j:j + wl]] += 1
                    count += 1
                    while Tdic[s[j:j + wl]] > dic[s[j:j + wl]]:
                        Tdic[s[head: head + wl]] -= 1
                        count -= 1
                        head += wl
                else:
                    for k in Tdic.keys():
                        Tdic[k] = 0
                    count = 0
                    head = j + wl
                    if head >= len(s) - wl + 1:
                        break
                if count == cnt:
                    res.append(head)
        return res
        
