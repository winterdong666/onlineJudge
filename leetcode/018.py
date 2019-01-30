class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        if len(nums) < 4:
            return res
        
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] * 4 > target:
                break
            tmpTarget = target - nums[i]
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[j] * 3 > tmpTarget:
                    break
                l, r = j + 1, len(nums) - 1
                while l < r:
                    s = nums[j] + nums[l] + nums[r]
                    if s < tmpTarget:
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s == tmpTarget:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    else:
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
        return res
