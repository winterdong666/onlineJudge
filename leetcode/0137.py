'''
  one   two
1  x     0
2  0     x
3  0     0
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one, two = 0, 0
        for i in nums:
            one = (one ^ i) & ~two
            two = (two ^ i) & ~one
        return one
