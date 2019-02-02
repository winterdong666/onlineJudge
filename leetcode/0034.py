class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(nums) - 1
        find = False
        m = (l + r) // 2
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                find = True
                break
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        if not find:
            return [-1, -1]
        
        ll, lr = 0, m
        rl, rr = m, len(nums) - 1
        lm, rm = (ll + lr) // 2, (rl + rr) // 2
        while ll < lr:
            lm = (ll + lr) // 2
            if nums[lm] == target:
                lr = lm - 1
            else:
                ll = lm + 1
        while rl < rr:
            rm = (rl + rr) // 2
            if nums[rm] == target:
                rl = rm + 1
            else:
                rr = rm - 1
        while nums[lm] != target:
            lm += 1
        while nums[lm] == target and lm > 0:
            lm -= 1
            if nums[lm] != target:
                lm += 1
                break
        while nums[rm] != target:
            rm -= 1
        while nums[rm] == target and rm < len(nums) - 1:
            rm += 1
            if nums[rm] != target:
                rm -= 1
                break
        return [lm, rm]
