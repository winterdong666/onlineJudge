class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        start = 0
        char_to_pos = {}
        end = 1
        char_to_pos[s[start]] = start
        res = 1
        while end < len(s):
            if char_to_pos.get(s[end]) == None or char_to_pos[s[end]] < start:
                char_to_pos[s[end]] = end
            else:
                start = char_to_pos[s[end]] + 1
                char_to_pos[s[end]] = end
            res = max(res, end - start + 1)
            end = end + 1
        return res
