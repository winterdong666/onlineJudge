class Solution:
    def isPalindrome(self, s: 'str') -> 'bool':
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and s[i].isalpha() == False and s[i].isdigit() == False:
                i += 1
            while i < j and s[j].isalpha() == False and s[j].isdigit() == False:
                j -= 1
            if i >= j:
                break
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
