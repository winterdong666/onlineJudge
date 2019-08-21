class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for i in range(len(strs)):
            tmp = sorted(strs[i])
            tmp = tuple(tmp)
            if dic.get(tmp, 0) == 0:
                dic[tmp] = [strs[i]]
            else:
                dic[tmp].append(strs[i])
        res = []
        for i in dic.keys():
            res.append(dic[i])
        return res
        
                
