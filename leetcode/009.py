class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        sx = str(x)
        for i in range(len(sx) // 2):
            if sx[i] != sx[-(i + 1)]:
                return False
        return True
