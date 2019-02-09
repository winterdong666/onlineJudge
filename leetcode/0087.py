class Solution:
    def isScramble(self, s1: 'str', s2: 'str') -> 'bool':
        if s1 == s2:
            return True
        count = {}
        for i in s1:
            count[i] = count.get(i, 0) + 1
        for i in s2:
            count[i] = count.get(i, 0) - 1
        for i in count.keys():
            if count[i] != 0:
                return False
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) == True:
                return True
            if (self.isScramble(s1[:i], s2[len(s1) - i:]) and self.isScramble(s1[i:], s2[:len(s1) - i])) == True:
                return True
        return False
