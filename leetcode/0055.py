class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l, r = 0, nums[0]
        forward = False
        while r < len(nums) - 1:
            forward = False
            t = r
            for i in range(l, r + 1):
                t = max(t, i + nums[i])
                if t > r:
                    forward = True
            l = r
            r = t
            if forward == False:
                return False
        return True
